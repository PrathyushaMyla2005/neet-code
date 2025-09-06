'''Problem Statement

You are given two binary trees:

root (the big tree)

subRoot (the smaller tree)

We need to check whether subRoot is a subtree of root.

👉 A subtree of a tree is a node in the tree and all of its descendants.
So, if there’s any node in root such that the tree starting from that node is identical to subRoot, then return true. Otherwise, return false.

✅ Example 1
root = [3,4,5,1,2]
subRoot = [4,1,2]


Tree root:       3
      / \
     4   5
    / \
   1   2
    4
   / \
  1   2
Here, the subtree rooted at 4 in root is exactly same as subRoot.
✅ Answer = true.'''
'''Iterative Approach (BFS / DFS Traversal)
Idea:

Traverse the root tree using BFS (queue) or DFS (stack).

At each node, check if the subtree starting at that node is identical to subRoot.

This “check identical” part can also be done iteratively.

If any identical subtree is found → return true.

If traversal ends with no match → return false.

✅ Algorithm (Iterative BFS)

Use a queue to perform level-order traversal of root.

For each node:

If its value matches subRoot.val, call an iterative function isSameTreeIter(node, subRoot).

If true → return true.

Push left and right children into queue.

If queue empties → return false.
ime: O(m * n) in worst case (m = root size, n = subRoot size).

Space: O(max(h1, h2)) for queue (tree height).'''
from collections import deque

# Define a tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val       # value of the node
        self.left = left     # left child
        self.right = right   # right child

# Function to check if two trees are exactly the same
def isSameTreeIter(p, q):
    queue = deque([(p, q)])   # Use a queue to compare nodes in BFS order
                               # Store pairs of nodes (one from each tree)
    while queue:               # Loop until all nodes are checked
        n1, n2 = queue.popleft()   # Take the first pair from the queue
        
        # If both nodes are None, continue (both trees empty at this position)
        if not n1 and not n2:
            continue
        
        # If only one node is None → trees differ
        if not n1 or not n2:
            return False
        
        # If values are different → trees differ
        if n1.val != n2.val:
            return False
        
        # Add children pairs to the queue to compare next
        queue.append((n1.left, n2.left))
        queue.append((n1.right, n2.right))
    
    # All nodes matched → trees are identical
    return True

# Function to check if subRoot is a subtree of root
def isSubtree(root, subRoot):
    if not subRoot:       # Empty tree is always a subtree
        return True
    if not root:          # If main tree is empty but subRoot exists → False
        return False
    
    queue = deque([root]) # Start BFS with root of main tree
    while queue:          # Loop until all nodes are checked
        node = queue.popleft()  # Get next node from queue
        
        # If current node value matches subRoot root value
        if node.val == subRoot.val:
            # Check if subtree starting from this node matches subRoot
            if isSameTreeIter(node, subRoot):
                return True  # Found a matching subtree
        
        # Add children to queue to continue BFS
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    
    # If we finish BFS without finding a match → False
    return False

# -------------------------
# Example Trees
# Main Tree:
#         3
#        / \
#       4   5
#      / \
#     1   2
#
# SubTree:
#       4
#      / \
#     1   2
# -------------------------

# Build main tree
root = TreeNode(3)
root.left = TreeNode(4)
root.right = TreeNode(5)
root.left.left = TreeNode(1)
root.left.right = TreeNode(2)

# Build sub tree
subRoot = TreeNode(4)
subRoot.left = TreeNode(1)
subRoot.right = TreeNode(2)

# Check if subRoot is a subtree of root
result = isSubtree(root, subRoot)
print(result)  # Output: True
'''e + substring check
O(M + N)
O(M + N)'''
# Define a tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val       # Value of the node
        self.left = left     # Left child
        self.right = right   # Right child

# Function to serialize a tree into a string (Preorder traversal with null markers)
def serialize(root):
    if not root:
        return "#,"        # Use '#' to mark None nodes
    return str(root.val) + "," + serialize(root.left) + serialize(root.right)

# Optimized function to check if subRoot is a subtree of root
def isSubtreeOptimized(root, subRoot):
    root_serial = serialize(root)        # Serialize main tree
    sub_serial = serialize(subRoot)      # Serialize subtree
    return sub_serial in root_serial     # Check if subtree serialization exists in main tree

# -------------------------
# Example Trees
# Main Tree:
#         3
#        / \
#       4   5
#      / \
#     1   2
#
# SubTree:
#       4
#      / \
#     1   2
# -------------------------

# Build main tree
root = TreeNode(3)
root.left = TreeNode(4)
root.right = TreeNode(5)
root.left.left = TreeNode(1)
root.left.right = TreeNode(2)

# Build sub tree
subRoot = TreeNode(4)
subRoot.left = TreeNode(1)
subRoot.right = TreeNode(2)

# Check if subRoot is a subtree of root
result = isSubtreeOptimized(root, subRoot)
print(result)  # Output: True
