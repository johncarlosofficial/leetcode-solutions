from typing import Optional


# Definition for singly-linked list.
class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        if not head.next or not head.next.next:
            return head

        odd_pointer = head
        even_pointer = head.next

        odd_dummy_head = ListNode(0, odd_pointer)
        even_dummy_head = ListNode(0, even_pointer)

        while even_pointer.next and even_pointer.next.next:
            odd_pointer.next = odd_pointer.next.next
            even_pointer.next = even_pointer.next.next
            odd_pointer = odd_pointer.next
            even_pointer = even_pointer.next

        if even_pointer.next:
            odd_pointer.next = odd_pointer.next.next
            odd_pointer = odd_pointer.next

        even_pointer.next = None

        odd_pointer.next = even_dummy_head.next
        return odd_dummy_head.next
