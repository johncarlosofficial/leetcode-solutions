from python.p0083 import ListNode, Solution

a = ListNode(1)
b = ListNode(1)
c = ListNode(2)
d = ListNode(2)
e = ListNode(5)
f = ListNode(5)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

solution = Solution()
head = solution.deleteDuplicates(a)
