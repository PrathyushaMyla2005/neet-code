'''
Input: nums = [2,7,11,15], target = 9
Output: [0,1]  # because nums[0] + nums[1] = 2 + 7 = 9
🔹 Approach 1: Brute Force (Nested Loops)
Logic

Try every possible pair (i, j) and check if nums[i] + nums[j] == target.
Complexity

Time: O(n²) (check all pairs)

Space: O(1)

✅ Works, but very slow for large arrays.

'''
def twoSum(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(i+1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
'''
🔹 Approach 2: Hash Map (Optimal)
Logic

Use a dictionary to store numbers we’ve seen and their indices.

For each number num at index i:

Compute complement = target - num.

If complement already exists in dictionary → we found the answer.

Otherwise, store num with index in dictionary.
Complexity

Time: O(n) (one pass)

Space: O(n) (dictionary storage)

✅ This is the most efficient solution.

'''
def twoSum(nums, target):
    num_to_index = {}

    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_to_index:
            return [num_to_index[complement], i]
        num_to_index[num] = i
nums = [2, 7, 11, 15]
target = 9
print(twoSum(nums, target))   # [0, 1]

nums = [3, 2, 4]
target = 6
print(twoSum(nums, target)) 
def two_Sum(nums,target):
    hashMap = {}
    for i in range(0,len(nums)):
        search = target - nums[i]
        if search in hashMap:
            return [i,hashMap[search]]
        hashMap[nums[i]] = i
nums = [2, 7, 11, 15]
target = 9
print(two_Sum(nums,target))
'''✅ Final Answer

Time Complexity: O(n)

Space Complexity: O(n)
Time Complexity (T.C)

Let n = length of nums.

Loop runs once for each element → O(n)

Inside loop:

Dictionary lookup (search in hashMap) = O(1) average.

Dictionary insert (hashMap[nums[i]] = i) = O(1) average.

👉 Total T.C = O(n)

💾 Space Complexity (S.C)

We store elements in hashMap.

In worst case (when no solution until the end), we store all n numbers.

👉 Total S.C = O(n) '''