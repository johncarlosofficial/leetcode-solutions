from python.p0143 import LinkedList, Solution

list = LinkedList()
list.addNodes([1,2,5,8,9])
print(list.displayList(list.head))


solution = Solution()
new_head = solution.reorderList(list.head)

print(list.displayList(new_head))