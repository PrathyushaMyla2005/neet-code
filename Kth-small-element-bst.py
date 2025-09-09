'''Problem Statement

You are given the root of a Binary Search Tree (BST) and an integer k.
You need to return the k-th smallest element in the BST.

🔹 Example
        5
       / \
      3   6
     / \
    2   4
   /
  1


Inorder traversal = [1, 2, 3, 4, 5, 6]

k = 3 → 3rd smallest element = 3'''
'''Normally we do recursive inorder traversal (Left → Root → Right).
But recursion uses the system call stack (hidden stack).
In iterative approach, we explicitly use a stack data structure to simulate recursion.
nitialize an empty stack.

Set current = root.

While current is not null OR stack is not empty:

Keep pushing all left children into stack (move left).

When no more left, pop from stack → this is the next smallest element.

Decrement k.

If k == 0, return that element.

Move to the right child.
Time Complexity:

Worst case: O(N) (visit all nodes).

Average: O(H + k) (H = tree height, because we push/pop at most once per node).

Space Complexity:

O(H) (stack holds nodes along one path).'''
#optimal approach
# ------------------ TreeNode Class ------------------
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val        # Value of the current node
        self.left = left      # Left child
        self.right = right    # Right child


# ------------------ Kth Smallest Function ------------------
def kthSmallest(root: TreeNode, k: int) -> int:
    stack = []               # Stack to simulate recursion
    current = root           # Start from root node
    
    while True:
        # Step 1: Go to the leftmost node
        while current:
            stack.append(current)   # Push current node to stack
            current = current.left  # Keep going left
        
        # Step 2: Pop node from stack (smallest available node)
        current = stack.pop()
        k -= 1  # We found one more element in sorted order
        
        if k == 0:  # If k becomes 0 → this is the kth smallest element
            return current.val
        
        # Step 3: Move to the right child
        current = current.right


# ------------------ Example Usage ------------------
if __name__ == "__main__":
    """
    Constructing the BST:
            5
           / \
          3   6
         / \
        2   4
       /
      1
    """
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(6)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.left.left.left = TreeNode(1)

    k = 3
    result = kthSmallest(root, k)
    print(f"The {k}-th smallest element is: {result}")
'''Why this approach is optimal:

In-order traversal of a BST gives nodes in sorted order.

Recursive traversal is cleaner and simpler than iterative with a stack.

We stop recursion early when we reach the k-th smallest element → avoids visiting unnecessary nodes.

Time Complexity (T.C)

In the worst case, we might visit all nodes → O(n)

But on average, we stop after visiting k nodes → O(k)

Space Complexity (S.C)

Recursion stack → maximum depth = height of BST → O(h)

Balanced BST → O(log n)

Skewed BST → O(n)'''
#brute
# ------------------ TreeNode Class ------------------
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val        # Value of the node
        self.left = left      # Pointer to left child
        self.right = right    # Pointer to right child

# ------------------ Brute Force Approach ------------------
def kthSmallestBrute(root: TreeNode, k: int) -> int:
    nodes = []  # List to store all node values

    # Helper function to traverse BST in-order
    def traverse(node):
        if not node:
            return  # Base case: if node is None, stop
        traverse(node.left)         # Visit left subtree
        nodes.append(node.val)      # Collect current node value
        traverse(node.right)        # Visit right subtree

    traverse(root)                 # Start traversal from root
    nodes.sort()                   # Sort all values (optional if in-order)
    return nodes[k-1]              # Return k-th smallest (0-indexed)

# ------------------ Example Usage ------------------
if __name__ == "__main__":
    """
    Constructing the BST:
            5
           / \
          3   6
         / \
        2   4
       /
      1
    """
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(6)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.left.left.left = TreeNode(1)

    k = 3
    result = kthSmallestBrute(root, k)
    print(f"The {k}-th smallest element is: {result}")
'''Metric	Complexity
Time (T.C)	O(n log n) → for sorting (or O(n) if using in-order)
Space (S.C)	O(n) → storing all node values'''