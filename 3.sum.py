'''1) Problem (what they ask)

Given an integer array nums, return all unique triplets [a,b,c] such that a + b + c = 0.
Triplets must be unique (no duplicates), and order inside the result doesn’t matter.'''
'''The 3Sum problem asks us to find all unique triplets in an array whose sum equals 0.
Input:

nums = [-1, 0, 1, 2, -1, -4]


We need to find all unique triplets that add up to 0.

🔎 Step 1: Sort the array

Sorting helps us use the two pointer method.

Original: [-1, 0, 1, 2, -1, -4]
Sorted:   [-4, -1, -1, 0, 1, 2]
[[-1, -1, 2], [-1, 0, 1]]
'''
'''2) Approach A — Brute force (triple loop + set)

Idea: Try every (i,j,k) with i<j<k. When sum is 0, store the sorted triplet in a set to avoid duplicates.

Time Complexity: O(n^3) (three nested loops)
Space Complexity: O(u) for the set of unique triplets (output aside)'''
def three_sum(nums):
    n = len(nums)
    seen = set()
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if nums[i]+nums[j]+nums[k] == 0:
                    trip = tuple(sorted((nums[i],nums[j],nums[k])))
                    seen.add(trip)
    return [list(t) for t in seen]
nums = [-1, 0, 1, 2, -1, -4]
print(three_sum(nums))
'''✅ Approach 2: Hashing (Fix one number + 2Sum with HashSet)

Idea:

Fix one number → reduce problem to 2Sum.

For the remaining two numbers, use a HashSet to check if target - nums[j] exists.

Steps:

Loop through each number nums[i].

Set target = -nums[i].

Use a hashset to find two numbers in the rest of the array that sum to target.

Add triplets into a set (to avoid duplicates).

Time Complexity: O(n²)

Space Complexity: O(n)

Faster than brute force.'''
def three_sum(nums):
    res = set()
    n = len(nums)
    for i in range(n):
        seen = set()
        target = -nums[i]
        for j in range(i+1,n):
            needed = target - nums[j]
            if needed in seen:
                triplet = tuple(sorted([nums[i],nums[j],needed]))
                res.add(triplet)
nums = [-1, 0, 1, 2, -1, -4]
print(three_sum(nums))