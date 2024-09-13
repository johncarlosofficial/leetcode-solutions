from collections import deque
from typing import List, Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # If the tree is empty, return an empty list
        if not root:
            return []
        
        result = []
        queue = deque([root])  # Use deque for efficient queue operations
        
        while queue:
            level_size = len(queue)
            level = []
            
            for i in range(level_size):
                node = queue.popleft()  # Pop the front node from the queue
                level.append(node.val)  # Add the node's value to the current level list
                
                # Add the children of the current node to the queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            result.append(level)  # Append the current level to the result
        
        return result

        # Time complexity: O(n) where n is the number of nodes in the tree,
        # because we process each node exactly once.

        # Space complexity: O(n) due to the storage needed for the queue
        # and the result list, which in the worst case can hold all the nodes in the tree.
