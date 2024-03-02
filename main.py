from python.p0024 import ListNode, Solution

a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
a.next = b
b.next = c
c.next = d

solution = Solution()
print(solution.swapPairs(a))
