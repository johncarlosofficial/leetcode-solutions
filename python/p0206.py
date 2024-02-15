# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
      
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return None

        if not head.next:
            return head

        prev_node = None
        curr_node = head

        while curr_node:
            next_node = curr_node.next # Save reference to the next node
            curr_node.next = prev_node # Reverse the current node's pointer
            prev_node = curr_node # Update previous node to be the current node
            curr_node = next_node # Move to the next node

        return prev_node # Return the new head of the reversed linked list






