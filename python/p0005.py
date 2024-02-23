class Solution:
  def expandAroundCenter(self, s: str, left: int, right: int) -> str:
    """
    Expands around the center and returns the longest palindrome substring
    centered at the specified indices `left` and `right`.
    """
    while left >= 0 and right < len(s) and s[left] == s[right]:
      # Expand outwards as long as characters at left and right indices match
      left -= 1
      right += 1
    # Return the palindrome substring
    return s[left + 1:right]
  
  
  def longestPalindrome(self, s: str) -> str:
    """
    Finds and returns the longest palindromic substring in the given string `s`.
    """
    if len(s) == 0:
      return ""
  
    longest = ""
  
    for i in range(len(s)):
      # For odd-length palindromes
      palindrome1 = self.expandAroundCenter(s, i, i)
      # For even-length palindromes
      palindrome2 = self.expandAroundCenter(s, i, i + 1)
  
      # Update the longest palindrome if either of the palindromes found is longer
      if len(palindrome1) > len(longest):
        longest = palindrome1
      if len(palindrome2) > len(longest):
        longest = palindrome2
  
    return longest
