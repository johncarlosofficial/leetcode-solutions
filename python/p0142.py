from typing import Optional


class ListNode:

  def __init__(self, x, next=None):
    self.val = x
    self.next = next


class Solution:

  def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
    slow, fast = head, head

    while slow and fast:
      slow = slow.next if slow.next else None
      fast = fast.next.next if fast.next else None
      if slow == fast:
        break

    if not slow or not fast:
      return None
    else:
      fast = head
      while fast != slow:
        slow = slow.next
        fast = fast.next

      return slow
