'''ou are given:

A string s (the source).

A string t (the target).

👉 You need to find the smallest substring of s that contains all characters of t (including duplicates).
If no such substring exists, return an empty string "".

Example 1:Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation:

The substring "BANC" is the smallest substring in s which contains A, B, and C.
Time & Space Complexity

Time Complexity = O(n³)

Generating substrings: O(n²)

Checking with Counter (O(n))

→ Overall O(n³)

Space Complexity = O(n + m) (hashmaps for substring and target)'''
from collections import Counter

def minWindow_bruteforce(s: str, t: str) -> str:
    n = len(s)
    min_len = float("inf")   # start with infinity (very large number)
    result = ""

    # frequency map of target string
    t_count = Counter(t)

    # generate all substrings
    for i in range(n):
        for j in range(i, n):
            sub = s[i:j+1]            # substring from i to j
            sub_count = Counter(sub)  # frequency of current substring

            # check if substring contains all chars of t
            valid = True
            for ch in t_count:
                if sub_count[ch] < t_count[ch]:
                    valid = False
                    break

            # if valid and smaller length, update result
            if valid and (j - i + 1) < min_len:
                min_len = j - i + 1
                result = sub

    return result

# Example usage
s = "ADOBECODEBANC"
t = "ABC"
print(minWindow_bruteforce(s, t))  # Output: "BANC"
'''Two Pointers / Sliding Window Approach

Idea:

Use a window [left, right] that slides over s.

Expand right to include characters until all of t is covered.

Then, shrink left as much as possible while still covering t.

Keep track of the minimum length substring.'''
