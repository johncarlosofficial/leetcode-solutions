import heapq  # For heap operations
from typing import Optional  # For optional type hint
from collections import deque  # For efficient queue operations

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        heap = []  # To store level sums as negative values (for max-heap behavior)
        queue = deque([root])  # Queue for level order traversal

        # Traverse the tree level by level
        while queue:
            size = len(queue)  # Number of nodes at the current level
            cur_sum = 0  # Sum of current level
            for _ in range(size):
                popped = queue.pop()  # Get next node
                cur_sum += popped.val  # Add node value to level sum

                # Add children to queue for the next level
                if popped.left:
                    queue.appendleft(popped.left)
                if popped.right:
                    queue.appendleft(popped.right)

            # Add negative level sum to the heap
            heapq.heappush(heap, -cur_sum)

        # Pop k-1 largest sums
        for i in range(k-1):
            heapq.heappop(heap)

        return -heap[0]  # Return the kth largest sum
