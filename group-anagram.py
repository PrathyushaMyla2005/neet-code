from collections import defaultdict

# --------------------------------------------
# Solution 1: Sorting Based
# --------------------------------------------
def groupAnagrams_sort(words):
    anagrams = defaultdict(list)
    for word in words:
        # Sort each word → same key for anagrams
        key = ''.join(sorted(word))
        anagrams[key].append(word)
    return list(anagrams.values())

# Example Walkthrough (Sorting Based):
# Input: ["eat","tea","tan","ate","nat","bat"]
# "eat" → "aet" → {"aet": ["eat"]}
# "tea" → "aet" → {"aet": ["eat","tea"]}
# "tan" → "ant" → {"aet":[...], "ant":["tan"]}
# "ate" → "aet" → {"aet":["eat","tea","ate"], "ant":["tan"]}
# "nat" → "ant" → {"aet":[...], "ant":["tan","nat"]}
# "bat" → "abt" → {..., "abt":["bat"]}
# ✅ Output: [["eat","tea","ate"], ["tan","nat"], ["bat"]]
#
# Complexity:
#   Sorting each word: O(k log k)
#   For n words: O(n × k log k)
#   Space: O(n × k)


# --------------------------------------------
# Solution 2: Optimal (Character Count Based)
# --------------------------------------------
def groupAnagrams(words):
    anagrams = defaultdict(list)
    for word in words:
        count = [0] * 26  # frequency of letters a–z
        for char in word:
            count[ord(char) - ord('a')] += 1
        key = tuple(count)  # immutable → can be used as dict key
        anagrams[key].append(word)
    return list(anagrams.values())

# Example Walkthrough (Optimal):
# Input: ["eat","tea","tan","ate","nat","bat"]
# Word = "eat"
# counts = [1,0,0,...,1,...,1,...]  # 'a','e','t'
# key = (1,0,0,...,1,...,1,...) → grouped
# "tea","ate" → same key → grouped together
# "tan","nat" → another key
# "bat" → its own key
# ✅ Output: [["eat","tea","ate"], ["tan","nat"], ["bat"]]
#
# Complexity:
#   Counting characters: O(k) per word
#   For n words: O(n × k)
#   Space: O(n × k)
# 👉 Faster than sorting when words are long


# --------------------------------------------
# Test
# --------------------------------------------
print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
