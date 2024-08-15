from typing import List, Optional

class ListNode:
    # Represents a node in the linked list, holding a value and a reference to the next node
    def __init__(self, value=0, next_node=None):
        self.val = value
        self.next = next_node

class LinkedList:
    # Initializes an empty linked list with head and tail pointers
    def __init__(self):
        self.head = None
        self.tail = None

    # Adds nodes to the linked list from a list of integers
    def addNodes(self, values: List[int]):
        for i in range(len(values)):
            if not self.head:
                # If the list is empty, set the first node as both head and tail
                self.head = ListNode(values[i])
                self.tail = self.head
            else:
                # Add new node at the end and update the tail reference
                self.tail.next = ListNode(values[i])
                self.tail = self.tail.next
  
    # Displays the linked list in a readable format
    def display(self):
        current_node = self.head
        while current_node:
            print(f"{current_node.val} ->", end=" ")
            current_node = current_node.next
        print("None")

class Solution:
    # Removes the nth node from the end of the linked list and returns the updated head
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None

        # Dummy node helps to simplify edge cases (like removing the first node)
        dummy_node = ListNode()
        dummy_node.next = head

        # Initialize two pointers, both starting from the dummy node
        slow = fast = dummy_node

        # Move the 'fast' pointer n steps ahead
        for i in range(n):
            fast = fast.next

        # Move both pointers until 'fast' reaches the last node
        while fast.next:
            slow = slow.next
            fast = fast.next

        # 'slow.next' is the node to be removed; skip it
        slow.next = slow.next.next

        # Return the head of the updated list
        return dummy_node.next

# Case usage
linked_list = LinkedList()
linked_list.addNodes([1,2,3,4,5])
linked_list.addNodes([6,7,8])
linked_list.display()

solution = Solution()
solution.removeNthFromEnd(linked_list.head, 3)
linked_list.display()
