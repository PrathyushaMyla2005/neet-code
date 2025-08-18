'''Given two strings s and t, return true if t is an anagram of s, and false otherwise.

👉 An anagram means two words/strings have the same characters with the same frequency, but order can be different.

Example:

Input: s = "anagram", t = "nagaram"
Output: true

Input: s = "rat", t = "car"
Output: false
Approach 1: Brute Force (Sorting)
Logic

If lengths are different → immediately return false.

Sort both strings.

If they are identical → return true.
Complexity

Sorting takes O(n log n)

Space: O(1) (in-place sort in Python).

'''
#sorting
def isAnagram(s, t):
    if len(s) != len(t):
        return False
    return sorted(s) == sorted(t)

# Example
print(isAnagram("anagram", "nagaram"))  # True
print(isAnagram("rat", "car"))          # False
'''Approach 2: HashMap / Frequency Count (Optimal)
Logic

Count frequency of each character in both strings.

Compare counts. If equal → anagram.
Complexity

Counting each string → O(n)

Space: O(1) (fixed alphabet, at most 26 lowercase letters).
'''
def  is_anagram_hashmap(s1,s2):
    count1={}
    count2={}
    for char in s1:
        count1[char]=count1.get(char,0)+1
    for char in s2:  
        count2[char]=count2.get(char,0)+1
        return count1==count2
'''
Approach 3: Single HashMap (Efficient)
Logic

Use one dictionary.

Increment counts for s and decrement for t.

If all counts become zero → anagram.
HashMap (1 dict)
O(n)
O(1)
Most efficient

'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count = {}
        
        for char in s:
            count[char] = count.get(char, 0) + 1
        for char in t:
            count[char] = count.get(char, 0) - 1
        
        for val in count.values():
            if val != 0:
                return False
        return True
# Example
print(isAnagram("listen", "silent"))  # True
print(isAnagram("hello", "bello"))    # False