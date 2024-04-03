# Definition for singly-linked list.
class ListNode:

  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next


class Solution:

  def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
    if not head or left == right:
      return head

    dummy = ListNode(0)
    dummy.next = head
    prev = dummy

    # Move prev to the node before the left position
    for _ in range(left - 1):
      prev = prev.next

    # Reverse the nodes between left and right positions
    curr = prev.next
    for _ in range(right - left):
      temp = prev.next
      prev.next = curr.next
      curr.next = curr.next.next
      prev.next.next = temp

    return dummy.next
