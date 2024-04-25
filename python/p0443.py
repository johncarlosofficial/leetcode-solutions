from typing import List


class Solution:
  def compress(self, chars: List[str]) -> int:
    if len(chars) == 1:
      return 1
      
    seen = chars[0]
    count = 1
    ans_pointer = 0
    
    for i in range(1, len(chars)):
      if chars[i] != seen:
        chars[ans_pointer] = seen
        ans_pointer += 1
        if count > 1:
          count = str(count)
          for char in count:
            chars[ans_pointer] = char
            ans_pointer += 1
        count = 1
        seen = chars[i]
      else:
        count += 1

    chars[ans_pointer] = seen
    ans_pointer += 1
    if count > 1:
      count = str(count)
      for char in count:
        chars[ans_pointer] = char
        ans_pointer += 1
        
    chars = chars[:ans_pointer]

    return ans_pointer
        
