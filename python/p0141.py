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

class Solution2:
  def hasCycle(self, head: ListNode) -> bool:
    slow, fast = head, head

    # If the linked list has 0 or 1 nodes, it can't have a cycle
    if not head or not head.next:
      return False

    # Traverse the linked list with two pointers
    while fast is not None and fast.next is not None:
      # Move slow pointer by one step and fast pointer by two steps
      slow = slow.next
      fast = fast.next.next

      # If slow and fast pointers meet at some point, there's a cycle
      if slow == fast:
        return True

    return False



    
    
