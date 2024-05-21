class Solution:

  def gcdOfStrings(self, str1: str, str2: str) -> str:
    # Check if concatenated strings are equal
    if str1 + str2 != str2 + str1:
      return ""
    else:
      # Get lengths of the strings
      a = len(str1)
      b = len(str2)

      # Find GCD of lengths using Euclidean algorithm
      while b != 0:
        a, b = b, a % b

      # Return the common prefix
      return str1[:a]
