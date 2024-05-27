class Solution:

    def findTheDifference(self, s: str, t: str) -> str:
        # Calculate the sum of ASCII values for both strings
        sum_s = 0
        for char in s:
            sum_s += ord(char)
        sum_t = 0
        for char in t:
            sum_t += ord(char)

        # Convert the ASCII difference to the character
        return chr(sum_t - sum_s)
