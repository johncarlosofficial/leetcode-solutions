from python.p0142 import ListNode, Solution

a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = c

solution = Solution()
print(solution.detectCycle(a))