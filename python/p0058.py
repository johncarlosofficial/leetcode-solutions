class Solution:

  def lengthOfLastWord(self, s: str) -> int:
    pointer = len(s) - 1

    while s[pointer] == ' ' and pointer > -1:
      pointer -= 1

    ans = 0
    while s[pointer] != ' ' and pointer > -1:
      ans += 1
      pointer -= 1

    return ans
