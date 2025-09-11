'''ou are given the root of a binary tree.
A path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections.

The path must contain at least one node.

The path does not need to go through the root.

We want to find the maximum sum among all possible paths in the tree.

✅ Example 1
       1
      / \
     2   3


Possible paths:

[1] → sum = 1

[2] → sum = 2

[3] → sum = 3

[1 → 2] → sum = 3

[1 → 3] → sum = 4

[2 → 1 → 3] → sum = 6

👉 Maximum path sum = 6

✅ Example 2
      -10
      /  \
     9   20
        /  \
       15   7


Possible paths include:

[15] → 15

[7] → 7

[20 → 15] → 35

[20 → 7] → 27

[9] → 9

[20 → 15 → -10 → 9] → 34

Best path: [15 → 20 → 7] → 42

👉 Maximum path sum = 42'''
'''Idea

A path can start and end at any two nodes in the tree.

If we try brute force, we will:

Consider every node as a possible "highest point" (turning point) of a path.

For that node, compute all possible paths that pass through it.

Keep track of the maximum sum across all such paths.

So brute force means:
👉 For each node, compute the maximum path sum that passes through it.
Brute force is O(n²) → too slow for large trees (say 10⁵ nodes).

Optimal approach = O(n) using DFS (calculate in one pass, avoid recomputation).'''
# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        # Helper: compute max downward path starting from this node
        def maxDownwardPath(node):
            if not node:
                return 0
            return node.val + max(maxDownwardPath(node.left), maxDownwardPath(node.right), 0)

        # Helper: compute max path sum passing through a given node
        def maxPathAtNode(node):
            if not node:
                return float("-inf")
            # Max path sum passing through this node
            left = maxDownwardPath(node.left)
            right = maxDownwardPath(node.right)
            through_node = node.val + max(left, 0) + max(right, 0)

            # Recurse for left and right children
            left_max = maxPathAtNode(node.left)
            right_max = maxPathAtNode(node.right)

            return max(through_node, left_max, right_max)

        return maxPathAtNode(root)


# -------------------------------
# Example Usage
# -------------------------------

# Build the tree:
#        -10
#        /  \
#       9   20
#          /  \
#         15   7

root = TreeNode(-10)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

# Run solution
sol = Solution()
print("Maximum Path Sum:", sol.maxPathSum(root))  # Expected: 42
'''Previous approach called maxDownwardPath inside every node’s maxPathAtNode recursively.

This leads to recomputing the same paths many times.

Time Complexity: O(n²) in worst case (every node calls downward path on all children).

✅ This is inefficient for large trees.

Optimal Approach

We can compute both things in one recursion:

For each node, compute:

Max path going downward from this node (used by parent)

Update global max path sum if the best path passes through this node (may include left + node + right)

Use a global variable to keep track of the maximum path sum.

Key idea:

Each node returns max downward path to its parent

But also updates global answer for the path passing through itself
Time	O(n) → visit each node once
Space	O(h) → recursion stack, h = height of tree'''
# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val        # Value of the node
        self.left = left      # Pointer to left child
        self.right = right    # Pointer to right child

# Solution class
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        # Global variable to store maximum path sum
        self.max_sum = float("-inf")  # Start with very small number

        # Helper function: returns max downward path sum from this node
        def helper(node):
            if not node:
                return 0   # Base case: empty node contributes 0 to path sum

            # Recursively get max downward path from left child
            left = max(helper(node.left), 0)  # Ignore negative paths

            # Recursively get max downward path from right child
            right = max(helper(node.right), 0)  # Ignore negative paths

            # Path passing through this node (node + left + right)
            current_path = node.val + left + right

            # Update global maximum if current path is bigger
            self.max_sum = max(self.max_sum, current_path)

            # Return the maximum downward path including this node
            return node.val + max(left, right)  # Only one side can go up to parent

        # Start recursion from root
        helper(root)

        # After recursion, max_sum contains the answer
        return self.max_sum


# ------------------------------
# Build the example tree
# ------------------------------

root = TreeNode(-10)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

# ------------------------------
# Run solution
# ------------------------------

sol = Solution()
print("Maximum Path Sum:", sol.maxPathSum(root))  # Expected: 42
