from typing import List, Optional


class ListNode:

  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next


class LinkedList:

  def __init__(self):
    self.head = None

  def append(self, nums: list):
    for num in nums:
      new_node = ListNode(num)

      if not self.head:
        self.head = new_node

      else:
        curr_node = self.head

        while curr_node.next:
          curr_node = curr_node.next

        curr_node.next = new_node

  def display(self):
    curr_node = self.head

    while curr_node:
      print(curr_node.val, end=" -> ")
      curr_node = curr_node.next

    print("None")


class Solution:

  def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    if not lists:
      return None

    while len(lists) > 1:
      merged_lists = []

      for i in range(0, len(lists), 2):
        list1 = lists[i]
        list2 = lists[i + 1] if i + 1 < len(lists) else None
        merged_lists.append(self.mergeTwoLists(list1, list2))

      lists = merged_lists

    return lists[0]

  def mergeTwoLists(self, list1, list2):
    dummy_node = ListNode()
    curr_node = dummy_node

    while list1 and list2:
      if list1.val <= list2.val:
        curr_node.next = list1
        list1 = list1.next
      else:
        curr_node.next = list2
        list2 = list2.next
      curr_node = curr_node.next

    if list1:
      curr_node.next = list1

    elif list2:
      curr_node.next = list2

    return dummy_node.next
