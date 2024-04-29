from typing import List


class Solution:

  def uniqueOccurrences(self, arr: List[int]) -> bool:
    hash_map = {}

    for i in range(len(arr)):
      if arr[i] not in hash_map:
        hash_map[arr[i]] = 1
      else:
        hash_map[arr[i]] += 1

    freq = set()

    for value in hash_map.values():
      if value in freq:
        return False
      else:
        freq.add(value)

    return True
