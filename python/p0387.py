class Solution:

  def firstUniqChar(self, s: str) -> int:
    hash_map = {}
    for i in range(len(s)):
      if s[i] not in hash_map:
        hash_map[s[i]] = [i]
      else:
        hash_map[s[i]].append(i)

    for item in hash_map:
      if len(hash_map[item]) == 1:
        return hash_map[item][0]
    return -1
