'''Problem Statement (Simplified)

You are given:

A string s consisting of only uppercase English letters.

An integer k.

👉 You can replace at most k characters in the string with any other uppercase letter.
Your goal: Find the length of the longest substring that can be obtained where all characters are the same.

🔹 Example
Example 1:s = "ABAB", k = 2
We can replace the two 'B's with 'A's → "AAAA", length = 4

👉 For each pair (i, j) we spend O(n) to construct and analyze substring.
t.c = O(n2)×O(n)=O(n^3)
s.c = o(1)
'''
def repeating_char(word, k):
    max_length = 0
    n = len(word)
    for i in range(n):                     # start index
        for j in range(i, n):              # end index
            hashMap = {}
            for t in range(i, j + 1):      # substring word[i..j]
                if word[t] not in hashMap:
                    hashMap[word[t]] = 0
                hashMap[word[t]] += 1

            max_freq = max(hashMap.values())
            if (j - i + 1) - max_freq <= k:    # check replacements
                max_length = max(max_length, j - i + 1)

    return max_length


# Example
word = "AABABBA"
k = 1
print(repeating_char(word, k))   # Output: 4
'''Sliding Window Approach (Efficient)

Instead of restarting for each substring, we expand and shrink a single window:

Move the right pointer (j) → add character to window.

Keep track of the most frequent char in the window (max_freq).

If the window is invalid (window_length - max_freq > k),
shrink from the left pointer (i).

Otherwise, update max length.
👉 This way, each character is processed at most twice (once when entering, once when leaving window).

Time Complexity: O(n)

Space Complexity: O(26) (constant for alphabets)

👉 This way, each character is processed''' 
def repeating_char(word, k):
    hashMap = {}                  # to store character counts
    max_freq = 0                  # highest frequency char in current window
    max_len = 0                   # answer
    i = 0                         # left pointer

    for j in range(len(word)):    # right pointer expands window
        # add word[j] to hashMap
        if word[j] not in hashMap:
            hashMap[word[j]] = 0
        hashMap[word[j]] += 1

        # update max frequency seen so far
        max_freq = max(max_freq, hashMap[word[j]])

        # if window length - max_freq > k, shrink window from left
        while (j - i + 1) - max_freq > k:
            hashMap[word[i]] -= 1
            i += 1   # shrink from left

        # update result
        max_len = max(max_len, j - i + 1)

    return max_len


# Example
word = "AABABBA"
k = 1
print(repeating_char(word, k))   # Output: 4
'''🟢 Sliding Window Approach (Efficient)

Instead of restarting for each substring, we expand and shrink a single window:

Move the right pointer (j) → add character to window.

Keep track of the most frequent char in the window (max_freq).

If the window is invalid (window_length - max_freq > k),
shrink from the left pointer (i).

Otherwise, update max length.

👉 This way, each character is processed at most twice (once when entering, once when leaving window).

Time Complexity: O(n)
Space Complexity: O(26) (constant for alphabets)'''
def repeating_char(word, k):
    hashMap = {}                  # to store character counts
    max_freq = 0                  # highest frequency char in current window
    max_len = 0                   # answer
    i = 0                         # left pointer

    for j in range(len(word)):    # right pointer expands window
        # add word[j] to hashMap
        if word[j] not in hashMap:
            hashMap[word[j]] = 0
        hashMap[word[j]] += 1

        # update max frequency seen so far
        max_freq = max(max_freq, hashMap[word[j]])

        # if window length - max_freq > k, shrink window from left
        while (j - i + 1) - max_freq > k:
            hashMap[word[i]] -= 1
            i += 1   # shrink from left

        # update result
        max_len = max(max_len, j - i + 1)

    return max_len


# Example
word = "AABABBA"
k = 1
print(repeating_char(word, k))   # Output: 4