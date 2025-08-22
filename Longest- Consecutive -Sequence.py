'''📌 Problem Statement

Given an unsorted array of integers, find the length of the longest consecutive sequence.

A consecutive sequence means numbers that come one after another without gaps.

Example: [100, 4, 200, 1, 3, 2]

The consecutive sequence is [1, 2, 3, 4].

Length = 4.

✅ Example 1

Input:
nums = [100, 4, 200, 1, 3, 2]

Output:
4 (because [1,2,3,4] is the longest consecutive sequence).

✅ Example 2

Input:
nums = [0,3,7,2,5,8,4,6,0,1]

Output:
9 (because [0,1,2,3,4,5,6,7,8] is the longest).'''
'''
Approach 1: Sorting Method

Idea:

If we sort the array, then consecutive numbers will be next to each other.

We just loop and count the longest streak.

Steps:

Remove duplicates (since duplicates don’t help).

Sort the array.

Traverse the array:

If current number = previous number + 1 → increase streak.

Else reset streak.

Keep track of the maximum streak.

Example:

[100, 4, 200, 1, 3, 2]

After removing duplicates & sorting: [1, 2, 3, 4, 100, 200]

Consecutive streaks:

1,2,3,4 → length = 4

100 → length = 1

200 → length = 1

Answer = 4.

Complexity:

Sorting → O(n log n)

Traversing → O(n)

Total = O(n log n), Space = O(1) or O(n) (depending on if we use extra space for removing duplicates).

✅ Easy to implement, but not optimal.
'''
def longestConsecutive_sorting(nums):
    if not nums:
        return 0

    nums = sorted(set(nums))  # remove duplicates + sort
    longest_streak = 1
    current_streak = 1

    for i in range(1, len(nums)):
        if nums[i] == nums[i-1] + 1:
            current_streak += 1
        else:
            current_streak = 1   # reset streak

        longest_streak = max(longest_streak, current_streak)

    return longest_streak
# Example usage:
print(longestConsecutive_sorting([100, 4, 200, 1, 3, 2]))  # Output: 4
'''
Approach 2: HashSet Method
Approach 2: HashSet (Optimal O(n))

Idea:

Use a set to quickly check if a number exists.

For each number, check if it is the start of a sequence (i.e., num-1 is not in the set).

If yes, count how long the sequence goes (num, num+1, num+2…).

Steps:

Put all numbers in a HashSet → O(n).

For each number:

If (num-1) is not in the set → start new sequence.

Expand forward (num+1, num+2…) until numbers stop.

Track maximum length.

Example:

[100, 4, 200, 1, 3, 2]

HashSet = {100,4,200,1,3,2}

Check each number:

100 → start, but no 101 → length = 1

4 → not start (since 3 exists)

200 → start, but no 201 → length = 1

1 → start, expand → 2,3,4 → length = 4

Max = 4.

Complexity:

Building set → O(n)

Checking sequences → Each number visited once → O(n)

Total = O(n), Space = O(n)

✅ Best approach.
'''
class Solution:
    def longestConsecutive(self, nums):
        num_set = set(nums)
        longest_streak = 0

        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak

# Example usage:
solution_instance = Solution()
print(solution_instance.longestConsecutive([100, 4, 200, 1, 3, 2]))  # Output: 4
