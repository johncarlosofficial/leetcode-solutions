# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Initialize a variable to track the maximum diameter
        self.max_diameter = 0

        # Helper function to compute the height of the tree
        def height(node: Optional[TreeNode]) -> int:
            # Base case: if the node is None, return -1 (meaning no edges)
            if not node:
                return -1

            # Recursively compute the height of the left and right subtrees
            left_height = height(node.left)
            right_height = height(node.right)

            # Update the diameter at this node
            current_diameter = left_height + right_height + 2
            self.max_diameter = max(self.max_diameter, current_diameter)

            # Return the height of the current node (1 + the maximum of the two subtree heights)
            return 1 + max(left_height, right_height)

        # Call the helper function starting from the root
        height(root)

        # The final diameter is stored in self.max_diameter
        return self.max_diameter
        