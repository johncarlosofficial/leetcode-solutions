class Solution:

  def partitionString(self, s: str) -> int:
    seen = set()
    ans = 0

    for char in s:
      if char in seen:
        ans += 1
        seen = set(char)
      else:
        seen.add(char)

    return ans + 1
