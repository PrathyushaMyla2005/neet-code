'''Problem Statement

Question:
Given a binary tree, determine if it is a valid Binary Search Tree (BST).

Rules for a BST:

The left subtree of a node contains only nodes with values less than the node’s value.

The right subtree of a node contains only nodes with values greater than the node’s value.

Both left and right subtrees must also be BSTs.

No duplicate values are allowed.
  2
   / \
  1   3
Output: True (Valid BST)

markdown
Copy code
    5
   / \
  1   4
     / \
    3   6
Output: False (4 < 5 is not allowed in right subtree)
'''
'''Iterative Approach: Using Stack + Min/Max

Idea:

Each node has a valid range (low, high).

Use a stack to simulate recursion: store (node, low, high) in the stack.

Check if node value is within range; if yes, push children with updated ranges.

Why we use iterative?

Avoid recursion stack overflow (useful for very deep trees)

Explicit control over stack and ranges
Iterative Approach: Using Stack + Min/Max

Idea:

Each node has a valid range (low, high).

Use a stack to simulate recursion: store (node, low, high) in the stack.

Check if node value is within range; if yes, push children with updated ranges.

Why we use iterative?

Avoid recursion stack overflow (useful for very deep trees)

Explicit control over stack and ranges
ime Complexity	O(n) → visit each node once
Space Complexity	O(h) → max stack size = height of tree (h)

Note: Worst case (skewed tree) → O(n) space'''
# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val       # value of the current node
        self.left = left     # left child
        self.right = right   # right child

# Iterative function to validate if a binary tree is a BST
def isValidBST(root):
    if not root:
        return True  # An empty tree is considered a valid BST
    
    # Stack to store nodes along with their valid value ranges (min, max)
    # Each element is a tuple: (node, lower_bound, upper_bound)
    stack = [(root, float('-inf'), float('inf'))]
    
    # Loop until stack is empty
    while stack:
        node, low, high = stack.pop()  # Pop the top node and its valid range
        
        # Check if current node violates the BST property
        # Node value must be strictly between low and high
        if not (low < node.val < high):
            return False  # BST property violated
        
        # If right child exists, push it to stack with updated valid range
        # All values in right subtree must be greater than current node
        if node.right:
            stack.append((node.right, node.val, high))
        
        # If left child exists, push it to stack with updated valid range
        # All values in left subtree must be less than current node
        if node.left:
            stack.append((node.left, low, node.val))
    
    return True  # All nodes satisfy BST properties, so return True

# -----------------------------
# Example Tree 1 (Valid BST)
#       5
#      / \
#     3   7
#    / \   \
#   2   4   8
root1 = TreeNode(5)
root1.left = TreeNode(3)
root1.right = TreeNode(7)
root1.left.left = TreeNode(2)
root1.left.right = TreeNode(4)
root1.right.right = TreeNode(8)

print("Example Tree 1 is BST:", isValidBST(root1))  # Output: True

# -----------------------------
# Example Tree 2 (Invalid BST)
#       5
#      / \
#     3   7
#    / \   
#   2   6  <-- 6 in left subtree of 5 is invalid
root2 = TreeNode(5)
root2.left = TreeNode(3)
root2.right = TreeNode(7)
root2.left.left = TreeNode(2)
root2.left.right = TreeNode(6)

print("Example Tree 2 is BST:", isValidBST(root2))  # Output: False
'''Approach: Inorder Traversal
Idea

In a BST, inorder traversal (left → root → right) produces nodes in strictly increasing order.

So, if we traverse the tree inorder and check that each node value is greater than the previous, the tree is a valid BST.

No need to track min/max ranges explicitly.

Why this is optimal?

We visit each node once → O(n) time.

Only keep previous node value → O(h) space (recursion stack)

Simple and easy to implement.'''