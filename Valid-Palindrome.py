'''Question:
Given a string s, determine if it is a palindrome, considering only alphanumeric characters (letters and numbers) and ignoring cases.

Palindrome: A string that reads the same forward and backward.

Example:

"A man, a plan, a canal: Panama" → true (after removing non-alphanumeric and ignoring cases, it becomes "amanaplanacanalpanama")

"race a car" → false

Constraints to consider:

Ignore spaces, punctuation, or any symbols.

Case-insensitive comparison ('A' = 'a').'''
'''Approach 1: Using String Cleaning and Reversal

Idea:

Clean the string: remove non-alphanumeric characters and convert to lowercase.

Check if the cleaned string is equal to its reverse. '''
def isPalindrome(s):
    # Step 1: Clean the string
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    
    # Step 2: Check palindrome
    return cleaned == cleaned[::-1]

# Example
print(isPalindrome("A man, a plan, a canal: Panama"))  # True
'''Approach 2: Two-Pointer Technique (Optimized)

Idea:

Use two pointers, left and right, starting from both ends of the string.

Skip non-alphanumeric characters.

Compare characters ignoring case.'''
def valid_palindrome(s):
    left,right = 0 ,len(s)-1
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
print(isPalindrome("A man, a plan, a canal: Panama"))