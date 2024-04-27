class Solution:

  def closeStrings(self, word1: str, word2: str) -> bool:
    if len(word1) != len(word2):
      return False

    h1 = {}
    h2 = {}

    for i in range(len(word1)):
      if word1[i] in h1:
        h1[word1[i]] += 1
      else:
        h1[word1[i]] = 1

      if word2[i] in h2:
        h2[word2[i]] += 1
      else:
        h2[word2[i]] = 1

    if h1.keys() != h2.keys():
      return False

    h1 = list(h1.values())
    h2 = list(h2.values())

    h1.sort()
    h2.sort()

    if h1 == h2:
      return True

    return False
