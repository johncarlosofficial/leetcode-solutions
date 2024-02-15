from python.p0141 import ListNode, Solution

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
d.next = b

solution = Solution()
print(solution.hasCycle(a))