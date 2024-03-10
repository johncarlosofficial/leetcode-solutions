class Solution:

  def strStr(self, haystack: str, needle: str) -> int:
    if len(needle) > len(haystack):
      return -1

    a, b = 0, 0

    while a < len(haystack):
      if haystack[a] == needle[b]:
        if b == len(needle) - 1:
          return a - b
        else:
          b += 1
      else:
        a -= b
        b = 0

      a += 1

    return -1
