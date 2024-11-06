class Solution:
    def minChanges(self, s: str) -> int:
        left = 0
        right = 1

        ans = 0

        while right < len(s):
            if s[left] != s[right]:
                ans += 1

            right += 2
            left += 2

        return ans
        