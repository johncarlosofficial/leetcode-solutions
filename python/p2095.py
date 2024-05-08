from typing import Optional


# Definition for singly-linked list.
class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        if not head.next:
            return None

        dummy = head
        prev = ListNode(0, head)
        slow = fast = head

        while fast.next and fast.next.next:
            prev = prev.next
            slow = slow.next
            fast = fast.next.next

        if fast.next:
            prev = prev.next
            slow = slow.next

        prev.next = slow.next

        return dummy
