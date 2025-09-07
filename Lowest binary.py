'''Question: Lowest Common Ancestor of a Binary Search Tree

We are given:

A Binary Search Tree (BST).

Two different nodes p and q that are inside this BST.

We need to find their Lowest Common Ancestor (LCA).

🔹 What does “Lowest Common Ancestor” mean?

Ancestor: A node X is an ancestor of node Y if you can move from X down the tree (through left/right children) and reach Y.
👉 Example: In the tree below, 6 is an ancestor of 2, 4, 5, etc.

Common Ancestor: A node that is an ancestor of both p and q.
👉 Example: If p=3 and q=5, their common ancestors are {6, 2, 4}.

Lowest Common Ancestor: The ancestor that is furthest down (lowest in the tree) but still common to both.
👉 Example: For p=3 and q=5, the LCA = 4 (since 4 is the deepest node that is an ancestor of both).

🔹 Example BST
        6
       / \
      2   8
     / \ / \
    0  4 7  9
      / \
     3   5


Case 1: p = 2, q = 8 →
Path to 2 = [6 → 2]
Path to 8 = [6 → 8]
Common ancestors = {6}
✅ LCA = 6

Case 2: p = 2, q = 4 →
Path to 2 = [6 → 2]
Path to 4 = [6 → 2 → 4]
Common ancestors = {6, 2}
✅ LCA = 2

Case 3: p = 3, q = 5 →
Path to 3 = [6 → 2 → 4 → 3]
Path to 5 = [6 → 2 → 4 → 5]
Common ancestors = {6, 2, 4}
✅ LCA = 4'''
'''🔹 Why Iterative Approach?

Recursive solution is clean, but it uses function call stack space.

Iterative solution avoids recursion → saves space → only O(1) extra memory.

Both run in the same time complexity O(h), where h = height of the BST.

That’s why iterative is often preferred in interviews and real-world code.

🔹 Intuition of Iterative Approach

We use the BST property:

If both p and q are less than root, the LCA lies in the left subtree → move left.

If both p and q are greater than root, the LCA lies in the right subtree → move right.

Otherwise → root is the split point → this is the LCA.
ime Complexity (T.C):

O(h), where h = height of tree.

Balanced BST → O(log n)

Skewed BST → O(n)

Space Complexity (S.C):

O(1) → iterative uses no extra space.'''
# ------------------ Define TreeNode class ------------------
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        # Each node in the BST will have:
        # 1. a value (val)
        # 2. a left child (left)
        # 3. a right child (right)
        self.val = val
        self.left = left
        self.right = right


# ------------------ Lowest Common Ancestor Function ------------------
def lowestCommonAncestor(root, p, q):
    # Keep checking nodes until we return the answer
    while root:
        # Case 1: If both p and q are smaller than current root,
        # then LCA must be in the LEFT subtree
        if p.val < root.val and q.val < root.val:
            root = root.left   # move root to the left child

        # Case 2: If both p and q are greater than current root,
        # then LCA must be in the RIGHT subtree
        elif p.val > root.val and q.val > root.val:
            root = root.right  # move root to the right child

        # Case 3: Otherwise, we have found the split point:
        # - either p < root < q
        # - or root == p
        # - or root == q
        # This means root is the Lowest Common Ancestor
        else:
            return root


# ------------------ Main Example Execution ------------------
if __name__ == "__main__":
    # Constructing BST:
    #         6
    #        / \
    #       2   8
    #      / \ / \
    #     0  4 7  9
    #       / \
    #      3   5

    # Create root node
    root = TreeNode(6)

    # Left subtree of root
    root.left = TreeNode(2)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(4)
    root.left.right.left = TreeNode(3)
    root.left.right.right = TreeNode(5)

    # Right subtree of root
    root.right = TreeNode(8)
    root.right.left = TreeNode(7)
    root.right.right = TreeNode(9)


    # ---------- Example 1 ----------
    # Find LCA of nodes 2 and 8
    p = root.left        # Node 2
    q = root.right       # Node 8
    lca = lowestCommonAncestor(root, p, q)
    print(f"LCA of {p.val} and {q.val} = {lca.val}")  # Expected output: 6


    # ---------- Example 2 ----------
    # Find LCA of nodes 2 and 4
    p = root.left        # Node 2
    q = root.left.right  # Node 4
    lca = lowestCommonAncestor(root, p, q)
    print(f"LCA of {p.val} and {q.val} = {lca.val}")  # Expected output: 2


    # ---------- Example 3 ----------
    # Find LCA of nodes 3 and 5
    p = root.left.right.left    # Node 3
    q = root.left.right.right   # Node 5
    lca = lowestCommonAncestor(root, p, q)
    print(f"LCA of {p.val} and {q.val} = {lca.val}")  # Expected output: 4
'''Why Iterative Approach is Optimal

Recursive approach also works, but:

Each recursive call uses extra function stack space.

In the worst case (skewed tree), recursion depth = O(h) where h is tree height.

This may cause stack overflow for very large trees.

Iterative approach avoids recursion and directly moves through the tree.

Uses only a few variables (no extra stack).

More memory-efficient.

✅ So Iterative Approach = Optimal.
ime Complexity

Each step we move one level down the BST (either left or right).

In the worst case, we might go from root → leaf (height of tree).

Time Complexity = O(h), where h = height of tree.

For balanced BST → h = log n

For skewed BST → h = n

📌 Space Complexity

Iterative approach only uses constant variables (root, p, q).

Space Complexity = O(1) (best possible).'''
# ------------------ Define TreeNode class ------------------
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        # Each node has a value and optional left/right children
        self.val = val
        self.left = left
        self.right = right


# ------------------ Lowest Common Ancestor Function ------------------
def lowestCommonAncestor(root, p, q):
    # Loop until we return the LCA
    while root:
        # Case 1: both p and q are smaller than root → move LEFT
        if p.val < root.val and q.val < root.val:
            root = root.left

        # Case 2: both p and q are greater than root → move RIGHT
        elif p.val > root.val and q.val > root.val:
            root = root.right

        # Case 3: split point found → this root is the LCA
        else:
            return root


# ------------------ Main Example Execution ------------------
if __name__ == "__main__":
    # Constructing BST:
    #         6
    #        / \
    #       2   8
    #      / \ / \
    #     0  4 7  9
    #       / \
    #      3   5

    # Root node
    root = TreeNode(6)

    # Left subtree
    root.left = TreeNode(2)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(4)
    root.left.right.left = TreeNode(3)
    root.left.right.right = TreeNode(5)

    # Right subtree
    root.right = TreeNode(8)
    root.right.left = TreeNode(7)
    root.right.right = TreeNode(9)

    # ---------- Example 1 ----------
    p = root.left        # Node 2
    q = root.right       # Node 8
    lca = lowestCommonAncestor(root, p, q)
    print(f"LCA of {p.val} and {q.val} = {lca.val}")  # Output: 6

    # ---------- Example 2 ----------
    p = root.left        # Node 2
    q = root.left.right  # Node 4
    lca = lowestCommonAncestor(root, p, q)
    print(f"LCA of {p.val} and {q.val} = {lca.val}")  # Output: 2

    # ---------- Example 3 ----------
    p = root.left.right.left    # Node 3
    q = root.left.right.right   # Node 5
    lca = lowestCommonAncestor(root, p, q)
    print(f"LCA of {p.val} and {q.val} = {lca.val}")  # Output: 4
