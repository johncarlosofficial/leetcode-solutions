class Solution:
    def minimumSteps(self, s: str) -> int:
        swaps = 0
        left = 0

        for right in range(len(s)):
            if s[right] == "0":
                swaps += right - left
                left += 1

        return swaps