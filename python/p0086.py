from typing import Optional


# Definition for singly-linked list.
class ListNode:

  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next


class Solution:

  def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
    # left and right lists head
    dummy_left = ListNode()
    dummy_right = ListNode()

    cur_left = dummy_left
    cur_right = dummy_right

    # current node
    cur = head

    # linked list traversal
    while cur:
      if cur.val < x:
        cur_left.next = cur
        cur_left = cur_left.next
      else:
        cur_right.next = cur
        cur_right = cur_right.next
      cur = cur.next

    # connect lists
    cur_left.next = dummy_right.next
    cur_right.next = None

    return dummy_left.next
