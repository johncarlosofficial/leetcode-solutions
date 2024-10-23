from collections import deque
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None  
        
        queue = deque([[root]])

        while queue:
            total_sum = 0

            # Calculate the sum of all nodes at the current level
            for nodes in queue:
                total_sum += nodes[0].val
                if len(nodes) == 2:  # If there is a right child
                    total_sum += nodes[1].val

            sums = [total_sum] * len(queue)

            # Adjust the sums by removing the value of each node
            for i in range(len(queue)):
                sums[i] -= queue[i][0].val
                if len(queue[i]) == 2:
                    sums[i] -= queue[i][1].val

            # Update the node values to the new sums
            for i in range(len(queue)):
                for j in range(len(queue[i])):
                    queue[i][j].val = sums[i]

            # Process the next level of children
            level_length = len(queue)
            for _ in range(level_length):
                popped = queue.popleft()

                if popped[0].left and popped[0].right:
                    queue.append([popped[0].left, popped[0].right])
                if popped[0].left and not popped[0].right:
                    queue.append([popped[0].left])
                if popped[0].right and not popped[0].left:
                    queue.append([popped[0].right])

                # Handle the second node in the pair (if exists)
                if len(popped) == 2:
                    if popped[1].left and popped[1].right:
                        queue.append([popped[1].left, popped[1].right])
                    if popped[1].left and not popped[1].right:
                        queue.append([popped[1].left])
                    if popped[1].right and not popped[1].left:
                        queue.append([popped[1].right])

        return root
