from python.p0021 import LinkedList, Solution

list1 = LinkedList()
list1.append([1, 2, 4])

list2 = LinkedList()
list2.append([1, 3, 4])

solution = Solution()
new_head = solution.mergeTwoLists(list1.head, list2.head)

merged_list = LinkedList()
merged_list.head = new_head
merged_list.display()