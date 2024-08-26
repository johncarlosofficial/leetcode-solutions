# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Base case: If the tree is empty (root is None), return None
        if not root:
            return None

        # Store the left and right child nodes temporarily
        left = root.left
        right = root.right

        # Swap the left and right child nodes
        root.left = right
        root.right = left

        # Recursively invert the left subtree (which was originally the right subtree)
        self.invertTree(right)
        # Recursively invert the right subtree (which was originally the left subtree)
        self.invertTree(left)

        # Return the root node, which now represents the inverted tree
        return root
