from typing import List


class Solution:

  def longestCommonPrefix(self, strs: List[str]) -> str:
    prefix = strs[0]

    for i in range(1, len(strs)):
      temp = []
      for j in range(min(len(strs[i]), len(prefix))):
        if strs[i][j] == prefix[j]:
          temp.append(strs[i][j])
        else:
          break
      prefix = ''.join(temp)

    return prefix
