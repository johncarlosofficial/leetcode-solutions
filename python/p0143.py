from typing import List, Optional


class ListNode:
    """
    Represents a single node in a linked list.
    
    Attributes:
        val (int): The value stored in the node.
        next (ListNode): A reference to the next node in the list.
    """

    def __init__(self, val=0, next=None):
        self.val = val  # Store the node's value
        self.next = next  # Initialize the next node reference


class LinkedList:
    """
    Represents a linked list, a linear data structure where elements
    are connected by pointers.
    
    Attributes:
        head (ListNode): The first node in the linked list.
    """

    def __init__(self):
        self.head = None  # Initialize the list with no elements

    def append(self, nums: list):
        """
        Appends a list of numbers to the linked list.

        Args:
            nums (list): A list of integers to be added to the linked list.
        """
        for num in nums:
            new_node = ListNode(num)  # Create a new node with the given value

            if not self.head:  # If the list is empty, set the new node as the head
                self.head = new_node
            else:
                current_node = self.head  # Start at the head of the list

                # Traverse the list to find the last node
                while current_node.next:
                    current_node = current_node.next

                # Attach the new node to the end of the list
                current_node.next = new_node

    def display(self):
        """
        Prints out the values in the linked list in a readable format.
        """
        current_node = self.head  # Start at the head of the list

        # Traverse the list and print each value
        while current_node:
            print(current_node.val, end=" -> ")
            current_node = current_node.next

        print("None")  # Indicate the end of the list


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        # 1. Find the middle of the list using two pointers (slow and fast)
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next  # Move slow pointer by one step
            fast = fast.next.next  # Move fast pointer by two steps

        # 2. Split the list into two halves
        right_head = slow.next  # Start of the second half
        slow.next = None  # End the first half

        # 3. Reverse the second half of the list
        prev_node = None
        curr_node = right_head

        while curr_node:
            next_node = curr_node.next  # Store the next node
            curr_node.next = prev_node  # Reverse the link
            prev_node = curr_node  # Move prev_node to current node
            curr_node = next_node  # Move curr_node to next node

        right_head = prev_node  # right_head now points to the reversed list

        # 4. Merge the two halves, alternating nodes from each half
        left_head = head  # Pointer to the start of the first half

        # Temporary node to facilitate merging
        curr_node = ListNode()

        while left_head and right_head:
            # Store the next nodes
            next_left_head = left_head.next
            next_right_head = right_head.next

            # Link the current node to the next node from the first half
            curr_node.next = left_head
            curr_node = curr_node.next

            # Link the current node to the next node from the second half
            curr_node.next = right_head
            curr_node = curr_node.next

            # Move the pointers to the next nodes in each half
            left_head = next_left_head
            right_head = next_right_head

        # If there are any remaining nodes in the first or second half, append them
        if left_head:
            curr_node.next = left_head
        if right_head:
            curr_node.next = right_head


# Example usage:
list1 = LinkedList()

# Append some values to the linked list
list1.append([1, 2, 3, 4, 5])

# Display the original list
print("Original List:")
list1.display()

# Create an instance of the solution and reorder the list
solution = Solution()
solution.reorderList(list1.head)

# Display the reordered list
print("Reordered List:")
list1.display()
