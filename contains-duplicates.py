'''Approach 1: Brute Force (Nested Loops)
Logic:

Compare each element with every other element.

If a match is found → return true.

If no match after checking all → return false.
Time Complexity:

Outer loop = n

Inner loop = up to n

O(n²) worst case → not efficient for large arrays.

Space Complexity:

O(1) (no extra data structures).

✅ Works, but slow for big inputs.'''
def containduplicates(nums):
    n = len(nums)
    for i in range(n):
        for j in range(i+1,n):
            if nums[i] == nums[j]:
                return True
            return False
'''
Approach 2: Sorting
Logic:

If we sort the array, any duplicates will be next to each other.

Traverse the sorted array → check if nums[i] == nums[i+1].

If found → return true.
Time Complexity:

Sorting: O(n log n)

Traversal: O(n)

Total → O(n log n)

Space Complexity:

Depends on sorting:

Python’s sort() → O(1) (in-place, Timsort).

✅ Better than brute force, but sorting takes extra time.
'''
def containduplicates(nums):
    nums.sort()
    for  i in range(len(nums)-1):
        if nums[i] == nums[i+1]:
            return True
        return False
'''Approach 3: HashSet (Optimal)
Logic:

Use a set to store seen numbers.

While iterating:

If number already in set → duplicate found → return true.

Otherwise, add it to set.

If loop ends, return false.
Time Complexity:

Iteration: O(n)

Set operations (in, add) = O(1) average (hashing).

Total → O(n)

Space Complexity:

O(n) (worst case: if all numbers unique, store them all).

✅ Fastest and most commonly used approach.'''
def containsDuplicate(nums):
    seen = set()
    for num in nums: 
        if num in seen:       # already seen → duplicate
            return True
        seen.add(num)         # store new number
    return False
nums1 = [3, 1, 4, 2, 3]   # has duplicate (3 appears twice)
nums2 = [1, 2, 3, 4]      # no duplicate
nums3 = [7, 7, 7, 7]      # all duplicates
nums4 = []                # empty list (no duplicates)

print("nums1:", containsDuplicate(nums1))  # True
print("nums2:", containsDuplicate(nums2))  # False
print("nums3:", containsDuplicate(nums3))  # True
print("nums4:", containsDuplicate(nums4))  # False