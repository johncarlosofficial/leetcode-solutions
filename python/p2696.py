class Solution:
  def minLength(self, s: str) -> int:
    while True:
      stack = []
      modified = False  # Flag to track if any modifications were made
      for char in s:
        if stack and char == 'B' and stack[-1] == 'A':
          stack.pop()
          modified = True
        elif stack and char == 'D' and stack[-1] == 'C':
          stack.pop()
          modified = True
        else:
          stack.append(char)
      # If no modifications were made, break the loop
      if not modified:
        break
      # Update the string with the modified stack
      s = ''.join(stack)

    return len(stack)
