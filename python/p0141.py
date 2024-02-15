# Definition for singly-linked list.
class ListNode:
  def __init__(self, x = 0, next = None):
    self.val = x
    self.next = next
    
class Solution:
  def hasCycle(self, head: ListNode) -> bool:
    visited = set()
    curr = head

    # If the linked list has 0 or 1 nodes, it can't have a cycle
    if not curr or not curr.next:
      return False

    # Traverse the linked list until the current node is not None
    while curr.next:
      # If the current node is already visited, it means there is a cycle
      if curr in visited:
        return True
      else:
        visited.add(curr)
        curr = curr.next
        
    return False
    
    
