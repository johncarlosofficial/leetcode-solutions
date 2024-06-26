class Solution:

  def findRepeatedDnaSequences(self, s: str):
    if len(s) < 10:
      return 0

    # Set to store encountered sequences
    hash_set = set()

    # Set to store repeated sequences
    ans_set = set()

    for i in range(len(s) - 9):
      if s[i:i + 10] in hash_set:
        ans_set.add(s[i:i + 10])
      else:
        hash_set.add(s[i:i + 10])

    return list(ans_set)
