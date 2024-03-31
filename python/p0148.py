from typing import Optional


# Definition for singly-linked list.
class ListNode:

  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next


class Solution:

  def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    if not head or not head.next:
      return head

    # Find the middle of the list
    mid = self.find_middle(head)

    # Split the list into two halves
    left_half = head
    right_half = mid.next
    mid.next = None

    # Recursively sort each half
    left_sorted = self.sortList(left_half)
    right_sorted = self.sortList(right_half)

    # Merge the sorted halves
    return self.merge(left_sorted, right_sorted)

  def find_middle(self, head: ListNode) -> ListNode:
    slow = head
    fast = head.next

    while fast and fast.next:
      slow = slow.next
      fast = fast.next.next

    return slow

  def merge(self, left: ListNode, right: ListNode) -> ListNode:
    dummy = ListNode()
    current = dummy

    while left and right:
      if left.val < right.val:
        current.next = left
        left = left.next
      else:
        current.next = right
        right = right.next
      current = current.next

    if left:
      current.next = left
    if right:
      current.next = right

    return dummy.next
