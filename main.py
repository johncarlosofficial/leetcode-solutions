from python.p0206 import ListNode, Solution

a = ListNode()
b = ListNode()
c = ListNode()
d = ListNode()

a.val = 1
a.next = b
b.val = 2
b.next = c
c.val = 3
c.next = d
d.val = 4

solution = Solution()
new_head = solution.reverseList(a)

curr_node = new_head

while curr_node:
  print(curr_node.val, end = " -> ")
  curr_node = curr_node.next
print("None")