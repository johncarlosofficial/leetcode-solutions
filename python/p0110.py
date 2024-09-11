# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        isBalanced = True  # Assume the tree is balanced initially

        # Helper function to calculate height and check balance
        def height(node):
            nonlocal isBalanced  # Access outer `isBalanced` variable
            
            if not node:
                return 0  # Base case: height of an empty tree is 0

            left_height = height(node.left)   # Recursively get left subtree height
            right_height = height(node.right) # Recursively get right subtree height

            # If height difference > 1, the tree is not balanced
            if abs(left_height - right_height) > 1:
                isBalanced = False

            # Return the height of the current node
            return 1 + max(left_height, right_height)

        height(root)  # Start the recursion from the root
        return isBalanced  # Return the final balance status

# Time Complexity: O(n) - We visit each node once to calculate its height and check the balance condition.
# Space Complexity: O(h) - Where h is the height of the tree. In the worst case (unbalanced tree), the recursion stack could go as deep as the height of the tree.
