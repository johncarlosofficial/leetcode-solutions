class Solution:

  def longestValidParentheses(self, s: str) -> int:
    stack = [
        -1
    ]  # Initialize with -1 to handle edge cases where first parentheses is closing
    size = 0
    longest = 0

    for i in range(len(s)):
      if s[i] == '(':
        stack.append(i)
      else:  # Character is ')'
        stack.pop()
        if not stack:
          stack.append(i)  # The beginning of a new substring
        else:
          size = i - stack[-1]
          longest = max(longest, size)

    return longest
