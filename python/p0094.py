# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        
        def traverse(node: Optional[TreeNode]):
            if node is None:
                return
            # Traverse the left subtree
            traverse(node.left)
            # Visit the root node
            result.append(node.val)
            # Traverse the right subtree
            traverse(node.right)
        
        # Start the traversal from the root node
        traverse(root)
        
        return result
