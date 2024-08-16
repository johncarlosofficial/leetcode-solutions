"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # If the head is None (the list is empty), return None immediately.
        if not head:
            return None

        # A dictionary to map original Nodes to their copies.
        # This helps us keep track of which Nodes have already been copied.
        originalToCopy = {None : None}

        # Step 1: Create a copy of each Node in the original list
        # without setting up their next and random pointers yet.
        cur = head
        while cur:
            # Create a new Node that is a copy of the current Node.
            copy = Node(cur.val)
            # Map the original Node to the copy.
            originalToCopy[cur] = copy
            # Move to the next Node in the original list.
            cur = cur.next

        # Step 2: Assign next and random pointers for the copied Nodes.
        cur = head
        while cur:
            copy = originalToCopy[cur]
            # Set the 'next' pointer of the copied Node to the copied version
            # of the original Node's 'next' pointer.
            copy.next = originalToCopy[cur.next]
            # Set the 'random' pointer of the copied Node to the copied version
            # of the original Node's 'random' pointer.
            copy.random = originalToCopy[cur.random]
            # Move to the next Node in the original list.
            cur = cur.next

        # Return the head of the copied linked list.
        return originalToCopy[head]