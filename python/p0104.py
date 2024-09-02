# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # If the tree is empty (root is None), the depth is 0
        if not root:
            return 0

        # Recursively find the maximum depth of the left and right subtrees.
        # Add 1 to account for the current node.
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        # The max function returns the larger of the two depths (left or right),
        # and adding 1 includes the current node in the depth count.
        