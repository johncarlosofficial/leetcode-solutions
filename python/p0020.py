class Solution:

  def isValid(self, s: str) -> bool:
    stack = []

    for char in s:
      # If the character is an opening bracket, push it onto the stack
      if (char == '(') or (char == '[') or (char == '{'):
        stack.append(char)
      # If the character is a closing bracket
      else:
        # Check if the stack is empty or the brackets don't match 
        if not stack or (char == ')' and stack[-1] != '(') or \
        (char == ']' and stack[-1] != '[') or \
        (char == '}' and stack[-1] != '{'):
          return False
        else:
          # Pop the matching opening bracket from the stack
          stack.pop()

    # If there are remaining brackets in the stack, the string is invalid
    if stack:
      return False

    return True