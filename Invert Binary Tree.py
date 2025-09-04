'''Problem: Invert Binary Tree

Question:
Given the root of a binary tree, invert the tree and return its root.

👉 Invert means: swap every left and right child in the tree.

🌳 Example
Input Tree:
        4
       / \
      2   7
     / \ / \
    1  3 6  9

Output Tree (Inverted):
        4
       / \
      7   2
     / \ / \
    9  6 3  1

🔑 Key Idea

'''
'''We need to invert (mirror) a binary tree.
That means → for every node, swap its left and right child.

There are two main ways to do this:

Recursive (DFS) → Go down the tree using recursion.

Iterative (BFS or DFS with stack/queue) → Use a loop instead of recursion.

We chose iterative BFS because:

It avoids recursion depth issues (safe for very deep trees).

BFS is easy to implement with a queue (deque).

We process nodes level by level → very straightforward.

👉 At each node, just swap children and continue.

⏱️ Time Complexity (T.C)

We visit each node exactly once.

At each node → only do a constant-time operation (swap).

So:

T.C = O(n)


where n = number of nodes in the tree.

📦 Space Complexity (S.C)

We use a queue to store nodes during BFS.

Worst case:

If the tree is very wide (like a complete binary tree), the queue may hold ~n/2 nodes (all nodes at thelast level).

So:

S.C = O(n)   (in worst case)
'''
from collections import deque   # deque is needed for efficient BFS queue operations

# ----------------------------
# Definition of a Binary Tree Node
# ----------------------------
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val          # store node value
        self.left = left        # pointer to left child
        self.right = right      # pointer to right child


# ----------------------------
# Iterative BFS approach to invert a binary tree
# ----------------------------
def invertTreeIterative(root):
    # Case 1: If the tree is empty, return None
    if not root:
        return None

    # Step 1: Initialize queue with root
    q = deque([root])

    # Step 2: Process nodes until queue is empty
    while q:
        # Take one node from the front of the queue
        node = q.popleft()

        # Step 3: Swap its left and right children
        node.left, node.right = node.right, node.left

        # Step 4: Add children to queue if they exist
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)

    # Step 5: Return the root of the inverted tree
    return root


# ----------------------------
# Helper function: BFS traversal to print tree in level order
# ----------------------------
def printLevelOrder(root):
    if not root:
        return []
    
    q = deque([root])   # queue initialized with root
    result = []         # list to store BFS result
    
    while q:
        node = q.popleft()
        result.append(node.val)
        
        # Add children if they exist
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
    
    return result


# ----------------------------
# Example Usage
# Build this tree:
#         4
#        / \
#       2   7
#      / \ / \
#     1  3 6  9
# ----------------------------
root = TreeNode(4)
root.left = TreeNode(2, TreeNode(1), TreeNode(3))
root.right = TreeNode(7, TreeNode(6), TreeNode(9))

print("Original Tree:", printLevelOrder(root))

# Invert using Iterative BFS
inverted_iter = invertTreeIterative(root)
print("Inverted Tree (Iterative):", printLevelOrder(inverted_iter))



'''Why do we use the recursive approach?

Natural fit for trees

Trees themselves are recursive structures (a tree is a node with two subtrees).

So recursion feels very natural: do the same thing on left subtree and right subtree.

Cleaner and shorter code

Only a few lines are needed.

Easier to read and understand than iterative with a queue.

Direct “divide & conquer” style

For each node: swap → let recursion handle the rest.

You don’t have to manually manage a queue or stack.
TC = O(n)
SC = O(h)'''
# ----------------------------
# Recursive function to invert a binary tree
# ----------------------------
def invertTreeRecursive(root):
    # Base case: if the node is None (empty tree or child), return None
    if not root:
        return None
    
    # Step 1: Recursively invert the left subtree
    left_inverted = invertTreeRecursive(root.left)
    
    # Step 2: Recursively invert the right subtree
    right_inverted = invertTreeRecursive(root.right)
    
    # Step 3: Swap the left and right children
    root.left, root.right = right_inverted, left_inverted
    
    # Step 4: Return the current root (with inverted children)
    return root
# ----------------------------
# Build the Example Tree Again (fresh tree, since previous one is already inverted):
#         4
#        / \
#       2   7
#      / \ / \
#     1  3 6  9
# ----------------------------
root2 = TreeNode(4)
root2.left = TreeNode(2, TreeNode(1), TreeNode(3))
root2.right = TreeNode(7, TreeNode(6), TreeNode(9))

# Print original tree in level order
print("Original Tree:", printLevelOrder(root2))

# Invert the tree using Recursive DFS
inverted_recursive = invertTreeRecursive(root2)

# Print inverted tree in level order
print("Inverted Tree (Recursive):", printLevelOrder(inverted_recursive))
