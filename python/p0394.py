class Solution:

  def decodeString(self, s: str) -> str:
    stack_count = []
    stack_str = []
    decoded_str = ""
    count = 0

    for char in s:
      if char.isdigit():
        count = count * 10 + int(char)
      elif char == '[':
        stack_count.append(count)
        stack_str.append(decoded_str)
        count = 0
        decoded_str = ""
      elif char == ']':
        prev_str = stack_str.pop()
        repeat_count = stack_count.pop()
        decoded_str = prev_str + decoded_str * repeat_count
      else:
        decoded_str += char

    return decoded_str
