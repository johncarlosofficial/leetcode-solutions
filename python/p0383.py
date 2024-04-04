class Solution:

  def canConstruct(self, ransomNote: str, magazine: str) -> bool:
    hash_map = {}

    for char in magazine:
      if char in hash_map:
        hash_map[char] += 1
      else:
        hash_map[char] = 1

    for char in ransomNote:
      if char in hash_map:
        hash_map[char] -= 1
        if hash_map[char] == 0:
          del hash_map[char]
      else:
        return False

    return True
