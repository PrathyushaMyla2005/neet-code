'''ou are given two lists:

Preorder → tells us the order of visiting nodes as Root → Left → Right.

Inorder → tells us the order of visiting nodes as Left → Root → Right.

👉 From these two lists, we need to rebuild the original tree.'''
'''Idea:

Take the first element from preorder. That is the root.

Find that root’s position in inorder.

Elements to the left of root in inorder → belong to left subtree.

Elements to the right → belong to right subtree.

Recursively repeat the process for left and right subtrees.
Time Complexity:

Searching root in inorder takes O(n)

We do this for all n nodes → O(n²)

Space Complexity:

Recursion depth = height of tree = O(n) (worst case, skewed tree)

No extra storage except recursive stack → O(n)'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder, inorder):
        # If no elements, return None
        if not preorder or not inorder:
            return None

        # Step 1: Root is always the first element of preorder
        root_val = preorder[0]
        root = TreeNode(root_val)

        # Step 2: Find root index in inorder (linear search -> brute force)
        root_index = inorder.index(root_val)

        # Step 3: Split inorder into left and right subtrees
        left_inorder = inorder[:root_index]
        right_inorder = inorder[root_index+1:]

        # Step 4: Split preorder (skip root, take correct size for left subtree)
        left_preorder = preorder[1: 1 + len(left_inorder)]
        right_preorder = preorder[1 + len(left_inorder):]

        # Step 5: Recursively build left and right subtrees
        root.left = self.buildTree(left_preorder, left_inorder)
        root.right = self.buildTree(right_preorder, right_inorder)

        return root


# ------------------ Example ------------------

def printTree(root, level=0, prefix="Root: "):
    """Helper function to print the tree structure"""
    if root:
        print(" " * (level*4) + prefix + str(root.val))
        printTree(root.left, level+1, "L--- ")
        printTree(root.right, level+1, "R--- ")

# Example inputs
preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]

solution = Solution()
tree = solution.buildTree(preorder, inorder)

print("Constructed Binary Tree:")
printTree(tree)
'''Instead of searching in inorder every time, we can build a hashmap (dictionary) for inorder.

Key = node value

Value = index in inorder
👉 Then lookup becomes O(1) instead of O(n).

We also avoid slicing lists repeatedly. Instead, we use indices to represent subranges.
Complexity

Time Complexity (TC):

Each node is processed once → O(n).

Lookups in hashmap = O(1) each.
👉 Total = O(n)

Space Complexity (SC):

Hashmap = O(n)

Recursion stack = O(h) (worst O(n) if skewed tree, average O(log n))
👉 Total = O(n)'''
# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder, inorder):
        # Step 1: Build hashmap for inorder
        inorder_map = {val: idx for idx, val in enumerate(inorder)}

        # Step 2: Pointer for preorder
        self.pre_index = 0

        # Step 3: Recursive function
        def array_to_tree(left, right):
            # if no elements
            if left > right:
                return None

            # pick root
            root_val = preorder[self.pre_index]
            self.pre_index += 1

            root = TreeNode(root_val)

            # get inorder index
            idx = inorder_map[root_val]

            # build left and right subtrees
            root.left = array_to_tree(left, idx - 1)
            root.right = array_to_tree(idx + 1, right)

            return root

        # Step 4: build whole tree
        return array_to_tree(0, len(inorder) - 1)


# ---------------- Example ----------------

def printTree(root, level=0, prefix="Root: "):
    if root:
        print(" " * (level*4) + prefix + str(root.val))
        printTree(root.left, level+1, "L--- ")
        printTree(root.right, level+1, "R--- ")

preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]

solution = Solution()
tree = solution.buildTree(preorder, inorder)

print("Constructed Binary Tree:")
printTree(tree)
