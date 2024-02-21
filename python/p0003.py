class Solution:

  def lengthOfLongestSubstring(self, s: str) -> int:
    seen = set()

    # Sliding window technique
    left = 0
    right = 0

    longest = 0

    while right < len(s):
      if s[right] not in seen:
        seen.add(s[right])
        right += 1
        longest = max(longest, right - left)
      else:
        seen.remove(s[left])
        left += 1

    return longest
