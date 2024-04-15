from typing import List


class Solution:

  def findContentChildren(self, g: List[int], s: List[int]) -> int:
    content = 0
    if len(s) == 0:
      return content
    g.sort()
    s.sort()
    i = 0
    j = 0

    while j < len(s) and i < len(g):
      if s[j] >= g[i]:
        content += 1
        i += 1
        j += 1
      else:
        j += 1
    return content
