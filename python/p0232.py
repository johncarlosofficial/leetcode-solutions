class MyQueue:

  def __init__(self):
    self.stack1 = []
    self.stack2 = []

  def push(self, x: int) -> None:
    self.stack1.append(x)

  def pop(self) -> int:
    if len(self.stack2) > 0:
      return self.stack2.pop()
    elif len(self.stack2) == 0 and len(self.stack1) > 0:
      self.moveElements()
      return self.stack2.pop()
    return -1

  def peek(self) -> int:
    if len(self.stack2) > 0:
      return self.stack2[-1]
    elif len(self.stack2) == 0:
      self.moveElements()
      return self.stack2[-1]
    return -1

  def empty(self) -> bool:
    return len(self.stack1) == 0 and len(self.stack2) == 0

  def moveElements(self):
    for _ in range(len(self.stack1)):
      self.stack2.append(self.stack1.pop())
