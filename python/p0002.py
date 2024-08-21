from typing import Optional
# Definition for singly-linked list node.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize a dummy node to keep track of the result's head
        dummy = ListNode()
        # 'current' points to the last node in the result list
        current = dummy

        carry = 0  # To store carry from the previous digit sum

        # Loop through both lists as long as both have nodes
        while list1 and list2:
            # Calculate the sum of current digits plus carry
            current_sum = list1.val + list2.val + carry
            # The new digit to add to the result list is the sum modulo 10
            new_digit = current_sum % 10
            # Update carry for the next iteration
            carry = current_sum // 10

            # Add the new digit to the result list
            current.next = ListNode(new_digit)
            current = current.next  # Move to the next node in the result list

            # Move to the next nodes in list1 and list2
            list1 = list1.next
            list2 = list2.next

        # If list1 is longer, continue adding its remaining digits
        while list1:
            current_sum = list1.val + carry
            new_digit = current_sum % 10
            carry = current_sum // 10

            current.next = ListNode(new_digit)
            current = current.next

            list1 = list1.next

        # If list2 is longer, continue adding its remaining digits
        while list2:
            current_sum = list2.val + carry
            new_digit = current_sum % 10
            carry = current_sum // 10

            current.next = ListNode(new_digit)
            current = current.next

            list2 = list2.next

        # If there's any carry left after processing both lists, add it as a new digit
        if carry != 0:
            current.next = ListNode(carry)

        # Return the result list, starting from the node after dummy
        return dummy.next