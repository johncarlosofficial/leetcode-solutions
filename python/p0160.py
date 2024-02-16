from typing import Optional


# Definition for singly-linked list.
class ListNode:

  def __init__(self, x):
    self.val = x
    self.next = None


class Solution:

  def getIntersectionNode(self, headA: ListNode,
                          headB: ListNode) -> Optional[ListNode]:
    # Initialize pointers and counters for both lists
    curr_a, size_a = headA, 1
    curr_b, size_b = headB, 1

    # Traverse list A to find its size
    while curr_a.next:
      curr_a = curr_a.next
      size_a += 1

    # Traverse list B to find its size
    while curr_b.next:
      curr_b = curr_b.next
      size_b += 1

    # If the last node of A is not the same as the last node of B, there's no intersection
    if curr_a != curr_b:
      return None

    # Reset pointers to the beginning of both lists
    curr_a, curr_b = headA, headB

    # Adjust the starting position of the longer list so they both have the same remaining length
    if size_a > size_b:
      diff = size_a - size_b
      for _ in range(diff):
        curr_a = curr_a.next
    elif size_b > size_a:
      diff = size_b - size_a
      for _ in range(diff):
        curr_b = curr_b.next

    # Traverse both lists in parallel until an intersection is found
    while curr_b != curr_a:
      curr_b = curr_b.next
      curr_a = curr_a.next

    # Return the intersection node (or None if no intersection is found)
    return curr_a
