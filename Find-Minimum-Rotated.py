'''🔹 Problem: Find Minimum in Rotated Sorted Array

👉 You are given an array of unique integers that was originally sorted in ascending order but rotated at some pivot.
You need to find the minimum element in this array.

✅ Example 1:
Input: nums = [3,4,5,1,2]
Output: 1
Explanation:
The original sorted array was [1,2,3,4,5].
It was rotated at index 3 → [3,4,5,1,2].
The minimum element is 1.

✅ Example 2:
Input: nums = [4,5,6,7,0,1,2]
Output: 0
Explanation:
Original sorted array was [0,1,2,4,5,6,7].
Rotated → [4,5,6,7,0,1,2].
Minimum element is 0.'''
'''🔹 Brute Force Approach
✅ Idea:

The problem asks us to find the minimum element in a rotated sorted array.

👉 The most straightforward way is:

Traverse the entire array.

Compare each element.

Keep track of the minimum.

Since we are not taking advantage of sorting/rotation, it works for any input.

✅ Steps:

Initialize a variable min_val with a very large value (like first element).

Loop through each element in the array.

Update min_val whenever a smaller element is found.

Return min_val after the loop ends.
✅ Time & Space Complexity:

Time Complexity (T.C):

We scan all n elements once.

So, O(n).

Space Complexity (S.C):

We only use one variable min_val.

So, O(1) (constant space).
'''
def findMin(nums):
    # Step 1: Assume first element is minimum
    min_val = nums[0]  
    
    # Step 2: Traverse the array
    for num in nums:
        if num < min_val:
            min_val = num  # Update min if found smaller
    
    # Step 3: Return the minimum
    return min_val
nums = [4,5,6,1,3,1]
print(findMin(nums))
'''Approach 2: Binary Search (Optimal)
✅ Idea:

The array is sorted but rotated.
That means the minimum element is the rotation point.

We can use binary search because the array has sorted segments.

✅ Steps:

Set two pointers: left = 0, right = n-1.

If the array is already sorted (first < last), then the first element is the minimum.

Otherwise:

Find mid = (left + right) // 2.

If nums[mid] > nums[right] → minimum lies right side.
So, left = mid + 1.

Else → minimum lies in the left side (including mid).
So, right = mid.

When left == right, that index is the minimum element.
✅ Time & Space Complexity:

Time Complexity: O(log n) (binary search)

Space Complexity: O(1) (no extra space)'''
def findMin(nums):
    left, right = 0, len(nums) - 1
    
    while left < right:
        mid = (left + right) // 2
        
        # If mid element > right element,
        # then min is in the right half
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            # min is in the left half (including mid)
            right = mid
    
    return nums[left]  # or nums[right], both same
nums = [4,5,67,1,0,1]
print(findMin(nums))