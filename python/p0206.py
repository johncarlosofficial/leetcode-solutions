# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val  # The value of the node
        self.next = next  # Pointer to the next node in the list

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # If the list is empty, return None
        if not head:
            return None

        # If the list has only one node, return that node
        if not head.next:
            return head

        prev_node = None  # This will become the new tail (initially None)
        curr_node = head  # Start with the head of the list

        # Iterate through the list until we reach the end
        while curr_node:
            next_node = curr_node.next  # Save reference to the next node
            curr_node.next = prev_node  # Reverse the current node's pointer
            prev_node = curr_node  # Update previous node to be the current node
            curr_node = next_node  # Move to the next node

        # The loop ends when curr_node is None (end of the list)
        # prev_node is now the new head of the reversed list
        return prev_node

# Example usage:
# Creating a linked list: 1 -> 2 -> 3 -> 4 -> 5 -> None
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

# Before reversal, the list is: 1 -> 2 -> 3 -> 4 -> 5 -> None
solution = Solution()
reversed_head = solution.reverseList(node1)

# After reversal, the list should be: 5 -> 4 -> 3 -> 2 -> 1 -> None
# Let's print the reversed list to verify
current = reversed_head
while current:
    print(current.val, end=" -> " if current.next else " -> None\n")
    current = current.next
