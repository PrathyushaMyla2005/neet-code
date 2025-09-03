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
'''from collections import deque   # deque = double-ended queue (fast for BFS)

# ---------------- TreeNode Class ----------------
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        # Each node has 3 parts:
        self.val = val          # the value stored in the node
        self.left = left        # pointer to left child (another TreeNode or None)
        self.right = right      # pointer to right child (another TreeNode or None)


# ---------------- Iterative Approach ----------------
def invertTreeIterative(root):
    # If the tree is empty, just return None
    if not root:
        return None

    # Start BFS with the root in queue
    q = deque([root])

    # Process nodes until queue becomes empty
    while q:
        # Take one node from the front of the queue
        node = q.popleft()

        # Core operation: swap its left and right child
        node.left, node.right = node.right, node.left

        # If left child exists, add it to queue to process later
        if node.left:
            q.append(node.left)

        # If right child exists, add it to queue to process later
        if node.right:
            q.append(node.right)

    # Finally, return the root of the inverted tree
    return root


# ---------------- Recursive Approach ----------------
def invertTreeRecursive(root):
    # Base case: if tree is empty, nothing to do
    if not root:
        return None

    # Core operation: swap left and right children of this node
    root.left, root.right = root.right, root.left

    # Recursively call function on left subtree
    invertTreeRecursive(root.left)

    # Recursively call function on right subtree
    invertTreeRecursive(root.right)

    # Return the root so the caller gets the inverted tree
    return root


# ---------------- Helper Function ----------------
def printLevelOrder(root):
    """Return tree in level-order (BFS) as a list of values."""
    if not root:
        return []
    q = deque([root])   # start with root in queue
    result = []
    while q:
        node = q.popleft()
        result.append(node.val)  # visit the node
        if node.left:            # add left child if exists
            q.append(node.left)
        if node.right:           # add right child if exists
            q.append(node.right)
    return result


# ---------------- Example Usage ----------------
# Build this tree:
#         4
#        / \
#       2   7
#      / \ / \
#     1  3 6  9

root1 = TreeNode(4)
root1.left = TreeNode(2, TreeNode(1), TreeNode(3))
root1.right = TreeNode(7, TreeNode(6), TreeNode(9))

print("Original Tree:", printLevelOrder(root1))

# --- Invert using Iterative approach ---
inverted_iter = invertTreeIterative(root1)
print("Inverted Tree (Iterative):", printLevelOrder(inverted_iter))

# Rebuild the tree again (because first one is already inverted)
root2 = TreeNode(4)
root2.left = TreeNode(2, TreeNode(1), TreeNode(3))
root2.right = TreeNode(7, TreeNode(6), TreeNode(9))

# --- Invert using Recursive approach ---
inverted_recur = invertTreeRecursive(root2)
print("Inverted Tree (Recursive):", printLevelOrder(inverted_recur))'''

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
from collections import deque   # deque is used for queue operations (faster than list)

# ----------------------------
# Definition of a Binary Tree Node
# ----------------------------
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val          # store the value of the node
        self.left = left        # pointer to the left child
        self.right = right      # pointer to the right child


# ----------------------------
# Function to invert (mirror) a binary tree iteratively
# ----------------------------
def invertTree(root):
    # Base case: if the tree is empty, return None
    if not root:
        return None
    
    # Step 1: Use a queue to perform level-order traversal (BFS)
    q = deque([root])  # Start with root node in the queue
    
    # Step 2: Keep processing until queue is empty
    while q:
        # Take out one node from the queue (FIFO order)
        node = q.popleft()
        
        # Step 3: Swap the left and right child of this node
        node.left, node.right = node.right, node.left
        
        # Step 4: If left child exists, push it into the queue
        if node.left:
            q.append(node.left)
        
        # Step 5: If right child exists, push it into the queue
        if node.right:
            q.append(node.right)
    
    # Step 6: Return the root of the inverted tree
    return root


# ----------------------------
# Helper function to print tree in Level-Order (BFS traversal)
# ----------------------------
def printLevelOrder(root):
    # If tree is empty, return empty list
    if not root:
        return []
    
    q = deque([root])  # start with root
    result = []        # to store level-order traversal
    
    while q:
        node = q.popleft()      # remove one node from queue
        result.append(node.val) # add its value to result
        
        # Push children if they exist
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
    
    return result   # return list of values in level-order


# ----------------------------
# Build the Example Tree:
#         4
#        / \
#       2   7
#      / \ / \
#     1  3 6  9
# ----------------------------
root = TreeNode(4)
root.left = TreeNode(2, TreeNode(1), TreeNode(3))   # Node 2 with children 1 and 3
root.right = TreeNode(7, TreeNode(6), TreeNode(9))  # Node 7 with children 6 and 9

# Print original tree in level order
print("Original Tree:", printLevelOrder(root))

# Invert the tree
inverted = invertTree(root)

# Print inverted tree in level order
print("Inverted Tree:", printLevelOrder(inverted))
