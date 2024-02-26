from python.p0019 import ListNode, Solution

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

solution = Solution()
new_head = solution.removeNthFromEnd(head, 3)

# Print the modified linked list
while new_head:
  print(new_head.val, end=" -> ")
  new_head = new_head.next

print("None")
