'''You are given two binary trees.
You need to check if they are the same.

Two binary trees are the same if:

They have the same structure (same shape).

The values of corresponding nodes are equal.

✅ Example 1:
Tree p:        Tree q:

     1              1
    / \            / \
   2   3          2   3


👉 Output: true
(Both trees are identical in shape and values).

✅ Example 2:
Tree p:        Tree q:

     1              1
    /                \
   2                  2


👉 Output: false
(Structure is different).'''
'''Step 1: Brute Force Idea

When we say brute force in tree problems, it usually means:
👉 Don’t directly compare trees node by node.
👉 Instead, convert both trees into some representation and then compare.

Brute Force Approach:

Traverse tree p (say in preorder) and store the traversal in a list/string (including null markers for missing children).

Traverse tree q in the same way.

Compare the two results:

If they are equal → trees are same.

Else → not same.

📌 Why do we use T.C and S.C?

T.C (Time Complexity) tells us how fast the algorithm runs (based on input size, not on a specific machine).

S.C (Space Complexity) tells us how much extra memory the algorithm uses (beyond the input).

👉 We use them to compare different solutions and pick the most efficient one.

Example:

If one solution runs in O(n) but another runs in O(n^2), the first is better.

If one uses O(1) extra memory but another uses O(n), the first is more memory-efficient.'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def serialize(self, root):
        """Preorder traversal with null markers"""
        if not root:
            return "N"   # Null marker for empty child
        return str(root.val) + "," + self.serialize(root.left) + "," + self.serialize(root.right)

    def isSameTree(self, p, q):
        return self.serialize(p) == self.serialize(q)

# Build Tree p
p = TreeNode(1)
p.left = TreeNode(2)
p.right = TreeNode(3)

# Build Tree q (same structure & values)
q = TreeNode(1)
q.left = TreeNode(2)
q.right = TreeNode(3)

# Run the solution
sol = Solution()
print(sol.isSameTree(p, q))   # Output: True
#T.C. = O(n)
#Time Complexity = O(n) → must check each node once.

#Space Complexity = O(h) → recursion depth depends on tree height.
# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p, q):
        # Case 1: both nodes are None → trees match at this branch
        if not p and not q:
            return True

        # Case 2: one node is None but not the other → mismatch
        if not p or not q:
            return False

        # Case 3: values don't match → mismatch
        if p.val != q.val:
            return False

        # Case 4: values match → check left & right subtrees
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


# 🌳 Example 1: Same Trees
p = TreeNode(1)
p.left = TreeNode(2)
p.right = TreeNode(3)

q = TreeNode(1)
q.left = TreeNode(2)
q.right = TreeNode(3)

sol = Solution()
print(sol.isSameTree(p, q))   # Output: True


# 🌳 Example 2: Different Trees
p2 = TreeNode(1)
p2.left = TreeNode(2)

q2 = TreeNode(1)
q2.right = TreeNode(2)

print(sol.isSameTree(p2, q2))  # Output: False
