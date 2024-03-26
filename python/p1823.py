class ListNode:

  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next


class LinkedList:

  def __init__(self):
    self.head = None

  def push(self, nums: int):
    if nums == 0:
      return
    self.head = ListNode(1)
    cur = self.head
    for i in range(2, nums + 1):
      cur.next = ListNode(i)
      cur = cur.next
    cur.next = self.head

  def output(self, node: ListNode):
    if not node:
      return
    cur = node
    while True:
      print(cur.val, end=" -> ")
      cur = cur.next
      if cur == node:
        break
    print()


class Solution:

  def findTheWinner(self, n: int, k: int) -> int:
    players = LinkedList()
    players.push(n)

    cur = players.head

    while cur.next != cur:
      for _ in range(k - 1):
        cur = cur.next
      cur.val = cur.next.val
      cur.next = cur.next.next

    return cur.val
