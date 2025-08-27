'''Longest Substring Without Repeating Characters

👉 You are given a string s. Find the length of the longest substring that contains no repeating characters.

A substring = continuous part of the string.

We just need the length, not the substring itself.

Example 1

Input: "abcabcbb"
Output: 3
Explanation: "abc" is the longest substring without repeating characters.


Example 2

Input: "bbbbb"
Output: 1
Explanation: "b" is the longest substring without repeating characters.


Example 3

Input: "pwwkew"
Output: 3
Explanation: "wke" is the longest substring without repeating characters.

🔹 Approaches
1. Brute Force (O(n³))

Generate all substrings.

For each substring, check if it has unique characters.

Track the maximum length.

Why bad? → Very slow for long strings (nested loops + uniqueness check).

2. Brute Force with Set Optimization (O(n²))

Fix a starting index i.

Expand substring by moving j forward.

Use a set to track unique characters in current substring.

If duplicate found → break.

Update max_length.

Why better? → Avoids inner-most checking loop, but still quadratic.'''
def substring_char(word):
    max_length =0
    n = len(word)
    for i in range(n):
        for j in range(i,n):
            hashset = set()
            flag = 0
            for k in range(i,j+1):
                if word[k] in hashset:
                    flag = 1
                    break
                else:
                    hashset.add(word[k])
            if flag == 0: #only unique substring
                max_length = max(max_length,j -i+1)
    return max_length
word=("abcabcbb")
print(substring_char(word))
'''🔹 Sliding Window Approach

✅ Idea:

Use two pointers (left and right) to represent a window.

Expand right to add characters.

If a duplicate is found, shrink window by moving left.

Keep track of max length.
Time & Space Complexity

Time Complexity: O(n) → each character added & removed once.

Space Complexity: O(min(n, charset)) → set stores unique chars in window (for ASCII max 128).'''
def lengthOfLongestSubstring(s):
    i = 0
    max_length = 0
    hashset = set()
    for j in range(len(s)):
        while s[j] in hashset:
            hashset.remove(s[i])
            i += 1
        hashset.add(s[i])
        max_length = max(max_length,j - i + 1)
    return max_length

# Example
print(lengthOfLongestSubstring("abcabcbb"))  # Output: 3
print(lengthOfLongestSubstring("bbbbb"))     # Output: 1
print(lengthOfLongestSubstring("pwwkew"))    # Output: 3