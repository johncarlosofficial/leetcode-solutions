class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # If s1 is longer than s2, s1 can't be a permutation of any substring of s2
        if len(s1) > len(s2):
            return False

        # Create frequency count arrays for characters in s1 and the current window in s2
        map1 = [0] * 26  # Frequency count for s1
        map2 = [0] * 26  # Frequency count for the current window in s2

        # Populate map1 with the frequency of each character in s1
        for char in s1:
            map1[ord(char) - ord("a")] += 1

        # Initialize map2 with the frequency of characters in the first window of s2
        for i in range(len(s1)):
            map2[ord(s2[i]) - ord("a")] += 1

        left = 0  # Start index of the window
        right = len(s1) - 1  # End index of the window

        # Slide the window across s2
        while right < len(s2):
            # If the current window matches the frequency count of s1, return True
            if map2 == map1:
                return True

            # Remove the character going out of the window from map2
            map2[ord(s2[left]) - ord("a")] -= 1
            left += 1  # Move the window to the right

            right += 1  # Expand the window to the right
            if right < len(s2):
                # Add the new character coming into the window to map2
                map2[ord(s2[right]) - ord("a")] += 1

        # After sliding through s2, check if the last window matches
        return map2 == map1


solution = Solution()
print(solution.checkInclusion("ab", "eidboaoo"))
