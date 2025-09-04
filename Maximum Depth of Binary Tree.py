'''Problem Statement (NeetCode 75)

Given the root of a binary tree,
Return its maximum depth.

1️⃣ What is "Depth" of a Binary Tree?

The depth of a binary tree is the number of nodes along the longest path from the root down to the farthest leaf node.

👉 In simpler terms:

Start at the root → go down until you hit the deepest leaf.

Count how many nodes are along that path.

That’s the maximum depth (sometimes also called height).

2️⃣ Example
        3
       / \
      9   20
         /  \
        15   7


Path from root (3) → leaf (9): depth = 2

Path from root (3) → leaf (15): depth = 3

Path from root (3) → leaf (7): depth = 3

👉 Maximum depth = 3'''
'''
4️⃣ Approach

We solve it using Recursion (DFS).

Key Idea:

If the tree is empty (root = None) → depth = 0

Otherwise:

Compute the depth of left subtree

Compute the depth of right subtree

Take the maximum of those two depths and add 1 (for the current root node).
Time Complexity = O(N)

We visit each node exactly once.

N = number of nodes in the tree.

✅ Space Complexity = O(W)

Queue stores nodes level by level.

Worst case = O(N) (when tree is a perfect binary tree, last level has N/2 nodes).

So,

DFS Recursive: O(N) time, O(H) space (H = height of tree).

BFS Iterative: O(N) time, O(N) space in worst case.
'''
from collections import deque   # deque is used for efficient queue operations

# ----------------------------
# Definition of a Binary Tree Node
# ----------------------------
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val          # store the value of the node
        self.left = left        # pointer to the left child
        self.right = right      # pointer to the right child


# ----------------------------
# Solution Class
# ----------------------------
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # Case 1: If tree is empty, depth = 0
        if not root:
            return 0
        
        # Step 1: Initialize a queue for BFS, start with root
        q = deque([root])   # queue will store nodes level by level
        depth = 0           # depth counter
        
        # Step 2: Process until queue becomes empty
        while q:
            level_size = len(q)  # number of nodes in current level
            
            # Process all nodes in this level
            for _ in range(level_size):
                node = q.popleft()   # take out one node from queue (FIFO)
                
                # Add children of current node into queue (next level)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            # After finishing one full level, increase depth
            depth += 1
        
        # Step 3: Return the total depth
        return depth


# ----------------------------
# Example Tree
# ----------------------------
# Build this tree:
#         3
#        / \
#       9   20
#          /  \
#         15   7
# Expected max depth = 3
# ----------------------------

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20, TreeNode(15), TreeNode(7))

# Create Solution object
sol = Solution()

# Call function
print("Maximum Depth of Binary Tree:", sol.maxDepth(root))
'''When asked this question:

Start with recursive DFS (clean code).

Most natural fit for the problem.

Explain BFS approach.

“Another way is BFS level order traversal, where each level increases depth.”

Mention complexities clearly.

Time: O(N)

Space: O(H) for recursion OR O(N) for BFS queue.

4️⃣ Key Placement Tip
Time & Space Complexity

Time Complexity (T.C.): O(N)

We visit each node exactly once.

Space Complexity (S.C.): O(H)

H = height of tree (recursion stack).

Worst case (skewed tree): O(N)

Best case (balanced tree): O(log N)'''
from typing import Optional

# -------------------------
# Definition for a binary tree node
# -------------------------
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val        # node value
        self.left = left      # left child
        self.right = right    # right child


# -------------------------
# Solution Class
# -------------------------
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Base case: if tree is empty → depth = 0
        if not root:
            return 0
        
        # Recursive case:
        # 1 + maximum depth of left and right subtree
        left_depth = self.maxDepth(root.left)    # depth of left subtree
        right_depth = self.maxDepth(root.right)  # depth of right subtree
        
        return 1 + max(left_depth, right_depth)


# -------------------------
# Example Usage
# -------------------------

# Build this tree:
#         3
#        / \
#       9   20
#          /  \
#         15   7
#
# Expected depth = 3

root = TreeNode(3)
root.left = TreeNode(9)                          # left child of root
root.right = TreeNode(20, TreeNode(15), TreeNode(7))  # right child with children

# Create solution object
sol = Solution()

# Find max depth
print("Maximum Depth of Tree:", sol.maxDepth(root))
