from python.p0061 import ListNode, Solution

a = ListNode(1)
b = ListNode(2)
c = ListNode(3)

a.next = b
b.next = c

solution = Solution()
print(solution.rotateRight(a, 2))

