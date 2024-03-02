from typing import Optional


class ListNode:

  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next


class Solution:

  def rotateRight(self, head: Optional[ListNode],
                  k: int) -> Optional[ListNode]:
    if not head:
      return None

    if k == 0:
      return head

    size = 1
    cur = head

    while cur.next:
      size += 1
      cur = cur.next

    rotate = k % size

    if rotate == 0:
      return head

    slow, fast = head, head

    for _ in range(rotate):
      fast = fast.next

    while fast.next:
      slow = slow.next
      fast = fast.next

    new_head = slow.next
    fast.next = head
    slow.next = None

    return new_head
