'''🔹 Question: Search in Rotated Sorted Array (LeetCode #33)

You are given:

An array nums that was originally sorted in ascending order.

Then it was rotated at some unknown index (pivot).

Example: [0,1,2,4,5,6,7] rotated at pivot 3 → [4,5,6,7,0,1,2].

A target value that you need to search in the array.

👉 Task: Return the index of the target if found, otherwise return -1.

🔹 Why is this different from normal binary search?

In a normal sorted array, you could just apply binary search directly.
But here, the array is rotated, so it has a "break point".

Example:

Sorted (normal):   [0, 1, 2, 3, 4, 5, 6]  
Rotated:           [4, 5, 6, 0, 1, 2, 3]


See how after 6 it suddenly goes back to 0?
That’s the rotation point.

🔹 Example 1

Input:

nums = [4,5,6,7,0,1,2], target = 0


The array was [0,1,2,4,5,6,7] originally.

Rotated → [4,5,6,7,0,1,2].

We need to find index of 0.

Answer = 4 (since nums[4] = 0).'''
'''✅ Approach 1: Brute Force (Linear Search)

👉 Idea: Just check every element one by one until we find the target.

🔸 Algorithm

Loop through the array from index 0 to n-1.

If nums[i] == target, return i.

If not found, return -1.
Time & Space Complexity

T.C. = O(n) → we might scan the whole array.

S.C. = O(1) → no extra space.

👉 Why not best? Because the question expects us to use binary search (O(log n)) since the array is sorted & rotated.'''
def serch(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1

nums = [4,5,6,7,0,1,2]   # ✅ keep nums as a list
target = 0               # ✅ separate variable
print(serch(nums, target))  # ✅ proper function call
'''
Approach 2: Binary Search with Rotation Check (Optimal)

👉 Idea:
Even though the array is rotated, one half is always sorted.
We use binary search, but also check which half is sorted to decide where to search next.

🔸 Algorithm

Set left = 0, right = n-1.

While left <= right:

Find mid = (left+right)//2.

If nums[mid] == target: return mid.

Check which half is sorted:

If nums[left] <= nums[mid]:
→ Left half is sorted.
→ If target is in this range → move right = mid-1.
→ Else move left = mid+1.

Else:
→ Right half is sorted.
→ If target is in this range → move left = mid+1.
→ Else move right = mid-1.

If not found, return -1.
Time & Space Complexity

T.C. = O(log n) → each step halves the search space.

S.C. = O(1) → only a few variables used.

👉 This is the best approach because the array is partially sorted → binary search is ideal.
'''
def search(nums,target):
    left,right = 0,len(nums) - 1
    while left <= right:
        mid = (left+right)//2
        if nums[mid] == target:
            return mid
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid -1
            else:
                left = mid + 1
        else:
            # Right half is sorted
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    
    return -1
nums = [4,5,6,7,0,1,2]   # ✅ keep nums as a listgir
target = 0               # ✅ separate variable
print(serch(nums, target))  # ✅ proper function call