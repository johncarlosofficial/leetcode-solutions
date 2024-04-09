from typing import List, Optional


class ListNode:

  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next


class LinkedList:

  def __init__(self):
    self.head = None

  def addNodes(self, nums: List[int]) -> None:
    for num in nums:
      new_node = ListNode(num)
      if not self.head:
        self.head = new_node
      else:
        cur = self.head
        while cur.next:
          cur = cur.next
        cur.next = new_node

  def displayList(self, node: Optional[ListNode]) -> None:
    while node:
      print(node.val, end=" -> ")
      node = node.next


class Solution:

  def reorderList(self, head: Optional[ListNode]):
    if not head:
      return None

    # find middle node
    slow, fast = head, head

    while fast.next and fast.next.next:
      slow = slow.next
      fast = fast.next.next

    right_head = slow.next
    slow.next = None

    # reverse right partition
    prev_node = None
    cur_node = right_head

    while cur_node:
      next_node = cur_node.next
      cur_node.next = prev_node
      prev_node = cur_node
      cur_node = next_node

    right_head = prev_node

    # merge lists
    left = head
    right = right_head

    while right:
      next_left = left.next
      next_right = right.next

      left.next = right
      right.next = next_left

      left = next_left
      right = next_right

    return head
