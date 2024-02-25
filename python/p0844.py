class Solution:

  def finalText(self, text):
    stack = []

    for char in text:
      if char == '#' and len(stack) != 0:
        stack.pop()
      elif char == '#' and len(stack) == 0:
        pass
      else:
        stack.append(char)

    return stack

  def backspaceCompare(self, s: str, t: str) -> bool:
    stack_s = self.finalText(s)
    stack_t = self.finalText(t)

    return bool(stack_s == stack_t)
