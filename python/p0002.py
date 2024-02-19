from typing import Optional


# Definition for singly-linked list.
class ListNode:

  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next


class Solution:

  def addTwoNumbers(self, l1: Optional[ListNode],
                    l2: Optional[ListNode]) -> Optional[ListNode]:
    carry = 0
    curr1 = l1
    curr2 = l2
    ans_node = ListNode(0)
    curr_node = ans_node

    while curr1 or curr2 or carry:
      val1 = curr1.val if curr1 else 0
      val2 = curr2.val if curr2 else 0

      total = val1 + val2 + carry
      carry = total // 10
      remainer = total % 10

      curr_node.next = ListNode(remainer)
      curr_node = curr_node.next

      curr1 = curr1.next if curr1 else 0
      curr2 = curr2.next if curr2 else 0

    return ans_node.next
