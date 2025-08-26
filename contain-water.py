'''Problem: Container With Most Water
Given:

An array height[] of non-negative integers.

Each integer represents the height of a vertical line drawn at that index.

Lines are drawn on the x-axis at positions 0, 1, 2, …, n-1.

Goal:

Pick two lines that together with the x-axis form a container.

Maximize the amount of water the container can hold.

How Water Area is Calculated:

For lines at positions i and j:

Area of water
=
Width
×
Height
Area of water=Width×Height

Width = distance between lines = j - i

Height = height of the shorter line = min(height[i], height[j])

Visual Example:
Index:   0  1  2  3  4  5  6  7  8
Height: [1, 8, 6, 2, 5, 4, 8, 3, 7]


Imagine vertical sticks at these heights.

If we choose the stick at index 1 (height=8) and index 8 (height=7):

Width = 8 - 1 = 7

Height = min(8, 7) = 7

Area = 7 × 7 = 49 ✅

So, maximum water = 49 units.'''
'''Approach 1: Brute Force (Check all pairs)

Idea:

Try every possible pair of sticks.

Calculate the water area for each pair.

Keep track of the maximum area.
Time Complexity: O(n²) → because we check every pair.
Space Complexity: O(1) → only a few variable'''
def contain_water(height):
    n = len(height)
    max_area = 0
    for i in range(n):
        for j in range(i+1, n):
            # width = j - i
            # height = min(height[i], height[j])
            area = min(height[i], height[j]) * (j - i)
            max_area = max(max_area, area)
    return max_area

# Example
height = [22, 123, 4, 6, 7]
print(contain_water(height))   # should print the maximum area
'''Two Pointer Approach (Efficient)
Idea

The maximum area depends on width and height.

To get the maximum width, we start with:

One pointer at the left end (i = 0)

Another at the right end (j = n-1)

Then we move the smaller height pointer inward, hoping to find a taller line that may give a larger area.
Time Complexity

O(n) → much faster than brute force O(n²).

Why? Each pointer moves at most once through the array.
'''
def contain_water(height):
    i = 0
    j = len(height) - 1
    max_area = 0
    
    while i < j:
        width = j - i
        h = min(height[i], height[j])
        area = width * h
        
        # update max_area
        if area > max_area:
            max_area = area
        
        # move pointers
        if height[i] < height[j]:
            i += 1
        else:
            j -= 1
    
    return max_area

# Example
height = [22, 123, 4, 6, 7]
print(contain_water(height))   # Output: 88
