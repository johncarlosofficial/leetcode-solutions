from typing import Optional


class ListNode:

  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next


class Solution:

  def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
    dummy_node = ListNode(0)
    dummy_node.next = head
    prev_node = dummy_node

    while prev_node.next and prev_node.next.next:
      first_node = prev_node.next
      second_node = prev_node.next.next

      # Swapping nodes
      first_node.next = second_node.next
      second_node.next = first_node
      prev_node.next = second_node

      # Move prev_node to the next pair
      prev_node = first_node

    return dummy_node.next
