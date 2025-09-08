'''📌 Problem: Binary Tree Level Order Traversal

LeetCode #102

You are given the root of a binary tree. You need to return its level order traversal (also known as Breadth-First Search traversal).

👉 Level Order Traversal means:

Visit all nodes level by level from top to bottom.

At each level, visit nodes from left to right.
        3
       / \
      9   20
         /  \
        15   7

[
  [3],
  [9,20],
  [15,7]
]
Level 0: [3]

Level 1: [9, 20]

Level 2: [15, 7]'''
'''1. Using BFS (Queue) → Iterative Approach ✅ (Most common)

Use a queue to traverse the tree level by level.

Start with the root in the queue.

For each level:

Process all nodes in the queue (that belong to this level).

Add their children (left, right) into the queue.

Collect values of this level into a list.

👉 This is the standard approach.
Time & Space Complexity
⏱ Time Complexity (T.C):

Each node is visited once.

Each node is inserted and removed from queue once.

O(N) where N = number of nodes.

💾 Space Complexity (S.C):

Queue can hold at most O(N) nodes (in last level of tree).

Result list stores all node values (O(N)).

O(N) overall.'''
from collections import deque

# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def levelOrder(root):
    if not root:
        return []               # if tree is empty, return []

    result = []                 # final answer
    queue = deque([root])       # queue initialized with root

    while queue:                # keep processing until queue empty
        level = []              # store values of this level
        size = len(queue)       # number of nodes at this level

        for _ in range(size):   # process all nodes at this level
            node = queue.popleft()   # pop from queue
            level.append(node.val)   # store node value

            if node.left:            # if left child exists
                queue.append(node.left)
            if node.right:           # if right child exists
                queue.append(node.right)

        result.append(level)         # add this level to result

    return result


# ------------------------------
# Example usage
# Build the tree:
#         3
#        / \
#       9   20
#          /  \
#         15   7

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

# Run level order traversal
print(levelOrder(root))
'''📌 Approach 2: DFS (Depth-First Search) with Recursion
🔎 Idea

Normally DFS is used for preorder/inorder/postorder.

But we can also achieve level order by keeping track of the depth (level) of each node.

At each recursive call, we pass the current level.

We store the node’s value inside result[level].
Time Complexity (T.C)

Every node is visited exactly once → O(N).

📌 Space Complexity (S.C)

result stores all nodes → O(N).

Recursion call stack can go up to O(H) where H = height of tree.

Worst case (skewed tree): O(N)

Best case (balanced tree): O(log N)

So total = O(N).'''
# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def levelOrderDFS(root):
    result = []

    def dfs(node, level):
        if not node:
            return
        
        # If this level doesn't exist yet, create it
        if len(result) == level:
            result.append([])
        
        # Add current node value to its level
        result[level].append(node.val)
        
        # Recurse left and right with level+1
        dfs(node.left, level + 1)
        dfs(node.right, level + 1)

    dfs(root, 0)
    return result


# ------------------------------
# Example usage
# Build the tree:
#         3
#        / \
#       9   20
#          /  \
#         15   7

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print(levelOrderDFS(root))
