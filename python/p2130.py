from typing import List, Optional


class ListNode:

  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next


class LinkedList:

  def __init__(self):
    self.head = None
    self.tail = None

  def addNodes(self, nums: List[int]):
    for i in range(len(nums)):
      new_node = ListNode(nums[i])
      if not self.head:
        self.head = new_node
        self.tail = self.head
      else:
        self.tail.next = new_node
        self.tail = self.tail.next

  def displayList(self, head):
    curr_node = head
    while curr_node:
      print(curr_node.val, end=" -> ")
      curr_node = curr_node.next


class Solution:

  def pairSum(self, head: Optional[ListNode]):
    if not head:
      return None
    # 1. Find the middle node (use slow/fast approach)
    slow = fast = head

    while fast.next and fast.next.next:
      slow = slow.next
      fast = fast.next.next

    # 2. Reverse the right partition
    right_head = self.reverse(slow.next)

    # Avoid list cycle
    slow.next = None

    # 3. Traverse both lists and calculate the twin sum
    ans = 0
    while head:
      twin_sum = head.val + right_head.val
      ans = max(ans, twin_sum)
      head = head.next
      right_head = right_head.next

    # 4. Return the maximum sum.
    return ans

  def reverse(self, head):
    prev_node = None
    curr_node = head

    while curr_node:
      next_node = curr_node.next
      curr_node.next = prev_node
      prev_node = curr_node
      curr_node = next_node

    return prev_node
