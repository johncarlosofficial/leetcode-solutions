class Solution:
  def isPalindrome(self, s: str) -> bool:
      letters = []

      for char in s:
          if char.isalpha() or char.isdigit():
              letters.append(char.lower())

      left, right = 0, len(letters) - 1

      while left < right:
          if letters[left] != letters[right]:
              return False
          left += 1
          right -= 1

      return True
