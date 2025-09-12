'''The Problem Statement

You are given a binary tree.
Your task is to:

Serialize (convert) the binary tree into a string (or some format like list).

This makes it easy to store or send the tree over a network.

Deserialize (rebuild) the original binary tree from that string.

This ensures that we can reconstruct the exact same tree back.

🔹 Why do we need this?

Imagine:

You want to save a tree into a file/database.

You want to send a tree structure across a network (e.g., in distributed systems).

We can’t directly send a tree object → we need to convert it into a storable/transferable format (like a string or list).
Later, we should be able to recreate the exact tree back.

🔹 Example

Consider this tree:

       1
      / \
     2   3
        / \
       4   5

✅ Serialization

If we serialize this using level-order (BFS traversal):

"1,2,3,null,null,4,5"'''
'''We call this approach brute force because:

It’s the most straightforward method:

Use DFS (preorder) recursion to traverse the tree.

Append "null" for missing children.

Rebuild recursively during deserialization.

We are not optimizing memory or traversal.

We store "null" even for every missing node.

The serialized string is larger than necessary.

It’s easier to implement and understand compared to more advanced or optimized ways (like compact encoding without "null"s).

👉 In short: brute force is used first because it’s simple, clear, and guaranteed to work, even though it’s not the most space-efficient.
Time Complexity = O(N) for both serialization and deserialization
SC (serialize) = O(N + H)

Worst case → O(N)

Average case → O(N) (since string dominates anyway)'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Codec:
    # Serialize (Tree → String)
    def serialize(self, root):
        def dfs(node):
            if not node:
                return "null,"   # represent None as "null"
            return str(node.val) + "," + dfs(node.left) + dfs(node.right)
        
        return dfs(root)

    # Deserialize (String → Tree)
    def deserialize(self, data):
        values = data.split(",")   # split by comma
        self.index = 0             # global index for reading values

        def dfs():
            if values[self.index] == "null":
                self.index += 1
                return None
            node = TreeNode(int(values[self.index]))
            self.index += 1
            node.left = dfs()     # build left subtree
            node.right = dfs()    # build right subtree
            return node

        return dfs()


# --------------------------
# Example Usage
# --------------------------

# Build a sample tree manually:
#        1
#       / \
#      2   3
#         / \
#        4   5
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)

# Create codec object
codec = Codec()

# Serialize
serialized = codec.serialize(root)
print("Serialized Tree:", serialized)

# Deserialize
deserialized_root = codec.deserialize(serialized)

# To verify, print the deserialized tree in preorder
def preorder(node):
    if not node:
        return ["null"]
    return [str(node.val)] + preorder(node.left) + preorder(node.right)

print("Preorder of Deserialized Tree:", " ".join(preorder(deserialized_root)))
'''rute Force Recap

We stored preorder traversal as a string with "null".

This works fine, but string concatenation (str(node.val) + ...) is not optimal → it creates many intermediate strings.

Still correct, but a bit wasteful.

🔹 Optimal Approach

We improve the brute force in two ways:

Use a list instead of string concatenation → much faster.

Same preorder logic (Root → Left → Right).

During deserialization, use an iterator to avoid handling index manually.
ime Complexity (TC)

Serialize: Visits each node once → O(n)

Deserialize: Rebuilds each node once → O(n)
where n = number of nodes.

🔹 Space Complexity (SC)

Serialize: Stores traversal in a list of size O(n).

Deserialize: Builds tree nodes (O(n) extra).

Recursion stack: O(h) (where h is tree height).

Balanced tree → O(log n)

Skewed tree → O(n)

So, total space = O(n)'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Codec:
    # Serialize (Tree → String)
    def serialize(self, root):
        res = []

        def dfs(node):
            if not node:
                res.append("null")
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(res)

    # Deserialize (String → Tree)
    def deserialize(self, data):
        values = iter(data.split(","))   # iterator over values

        def dfs():
            val = next(values)
            if val == "null":
                return None
            node = TreeNode(int(val))
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()


# --------------------------
# Example Usage
# --------------------------
# Tree:
#        1
#       / \
#      2   3
#         / \
#        4   5
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)

codec = Codec()
serialized = codec.serialize(root)
print("Serialized Tree:", serialized)

deserialized_root = codec.deserialize(serialized)

# Verify using preorder traversal
def preorder(node):
    if not node:
        return ["null"]
    return [str(node.val)] + preorder(node.left) + preorder(node.right)

print("Preorder of Deserialized Tree:", " ".join(preorder(deserialized_root)))
