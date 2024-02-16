from python.p0160 import ListNode, Solution

a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)

a.next = b
b.next = c
c.next = d

e = ListNode(1)
f = ListNode(2)

e.next = f
f.next = c

solution = Solution()
print(solution.getIntersectionNode(a, e))
