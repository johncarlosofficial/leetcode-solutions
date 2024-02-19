from python.p0002 import ListNode, Solution

# Função para imprimir lista ligada
def print_linked_list(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")

# Criação de duas listas ligadas para teste
# Número 243
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

# Número 564
l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

# Testando a função addTwoNumbers
solution = Solution()
result = solution.addTwoNumbers(l1, l2)

# Imprimindo o resultado
print("Resultado da adição:")
print_linked_list(result)
