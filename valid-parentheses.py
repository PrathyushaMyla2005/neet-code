'''Problem: Valid Parentheses
Question:

You are given a string s containing just the characters:

'(', ')',

'{', '}',

'[', ']'.

Return true if the input string is valid. Otherwise, return false.

🔑 A string is valid if:

Every opening bracket has a matching closing bracket of the same type.

Example: "(" must be closed by ")".

Brackets are closed in the correct order.
Example: "({})" is valid, but "(}" is invalid.

Every closing bracket must correspond to the most recent unmatched opening bracket.

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true
Example 3:
vbnet
Copy code
Input: s = "(]"
Output: false'''
'''Why we use this approach?

Beginner-friendly: Very easy to understand, no need for stack knowledge.

Direct simulation: We literally “delete” valid pairs until nothing is left.

Good for small strings: Works fine for short input.

But 🚩 it’s not efficient for large inputs because each replace takes O(n), and we may repeat up to n times.
Time Complexity:

Each replace() is O(n).

We may run up to n/2 times (if pairs keep reducing slowly).

Worst case → O(n²).

Space Complexity:

String copies are created during replacement → O(n).'''
def is_valid(s):
    prev = None
    while prev != s:   # keep looping until no change
        prev = s
        s = s.replace("()", "").replace("{}", "").replace("[]", "")
    return s == ""

s = "({[{)}]})"
print(is_valid(s))
'''We need to check if a string containing only "(){}[]" is valid.
👉 Valid means:

Every opening bracket has a matching closing bracket.

Order must be correct. (LIFO – last opened must close first).

🔑 Idea (Stack Approach)

Use a stack (like a box where you push and pop).

Traverse each character:

If it is an opening bracket ((, {, [), push it into the stack.

If it is a closing bracket (), }, ]):

Check if stack is empty → invalid (nothing to match).

Otherwise, pop the top element from the stack and check:

Do they match? (ex: ( with ), { with }, [ with ])

If not matching → invalid.

After finishing:

If stack is empty → ✅ valid.

If stack is not empty → ❌ invalid.
This is the Optimal Stack-Based Approach (most common in placements / interviews).
Time Complexity

We go through each character once → O(n).

Each push/pop operation is O(1).

✅ TC = O(n)

💾 Space Complexity

Stack stores opening brackets → in the worst case (all open brackets like "(((("), stack has n elements.

✅ SC = O(n)'''
def is_valid(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in mapping:
            top = stack.pop() if stack else '#'
            if mapping[char] != top:
                return False
            else:
                stack.append(char)
    return not stack
s="({[]})"
print(is_valid(s))