# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        heights = {}  # Store the height of each node
        levels = {}   # Store nodes by their levels with corresponding depths

        # Calculate height and depth for each node
        self.calculateHeightDepth(root, 0, heights, levels)

        # Sort nodes at each level by depth in descending order
        for nodes in levels.values():
            nodes.sort(key=lambda x: x[1], reverse=True)

        # Process each query
        return [self.calculateQuery(query, heights, levels) for query in queries]

    def calculateHeightDepth(self, node, level, heights, levels):
        if not node:
            return -1
        
        # Record the height for the current node
        heights[node.val] = level

        # Recursively calculate depth for left and right children
        left_depth = self.calculateHeightDepth(node.left, level + 1, heights, levels)
        right_depth = self.calculateHeightDepth(node.right, level + 1, heights, levels)

        # Determine the current node's depth based on the maximum depth of its children
        node_depth = 1 + max(left_depth, right_depth)

        # Append the node's value and depth to the level list
        levels.setdefault(level, []).append((node.val, node_depth))

        return node_depth
    
    def calculateQuery(self, query, heights, levels):
        level = heights[query]
        nodes_at_level = levels[level]

        # Find the max depth for the level excluding the queried node
        for node, depth in nodes_at_level:
            if node != query:
                return level + depth

        # If the queried node is the only one at its level, return level - 1
        return level - 1
