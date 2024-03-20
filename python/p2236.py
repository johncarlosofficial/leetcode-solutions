from typing import List, Optional


class TreeNode:
  def __init__(self, val = 0, left = None, right = None):
    self.val = val
    self.left = left
    self.right = right

class Tree:
  def __init__(self):
    self.root = None

  def insert(self, nums: List):
    self.root = TreeNode(nums[0])
    self.root.left = TreeNode(nums[1])
    self.root.right = TreeNode(nums[2])

class Solution:
  def checkTree(self, root: Optional[TreeNode]) -> bool:
    if not root:
      return False
    
    elif root.val == root.left.val + root.right.val:
      return True
      
    return False