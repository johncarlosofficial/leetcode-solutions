from typing import Optional


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
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Merges two sorted linked lists into one sorted linked list.

        Args:
            list1 (ListNode): The head of the first sorted linked list.
            list2 (ListNode): The head of the second sorted linked list.

        Returns:
            ListNode: The head of the merged sorted linked list.
        """
        # Handle edge cases where one or both lists are empty
        if not list1 and not list2:
            return None  # Both lists are empty, return None

        if not list1:
            return list2  # Only the first list is empty, return the second list

        if not list2:
            return list1  # Only the second list is empty, return the first list

        # Create a dummy node to start the merged list
        new_head = ListNode()
        current_node = new_head  # This will be used to build the new list

        # Merge the two lists while both have elements
        while list1 and list2:
            if list1.val <= list2.val:
                current_node.next = list1  # Attach the smaller node to the merged list
                list1 = list1.next  # Move to the next node in list1
            else:
                current_node.next = list2  # Attach the smaller node to the merged list
                list2 = list2.next  # Move to the next node in list2

            current_node = current_node.next  # Move to the next position in the merged list

        # If there are remaining nodes in list1, attach them
        if list1:
            current_node.next = list1

        # If there are remaining nodes in list2, attach them
        if list2:
            current_node.next = list2

        return new_head.next  # Return the head of the merged list (skipping the dummy node)


# Example usage:
list1 = LinkedList()
list2 = LinkedList()

# Append some values to the linked lists
list1.append([1, 2, 4])
list2.append([1, 3, 4])

# Create an instance of the solution
solution = Solution()

# Merge the two linked lists and print the result
merged_list_head = solution.mergeTwoLists(list1.head, list2.head)
merged_list = LinkedList()
merged_list.head = merged_list_head
merged_list.display()
