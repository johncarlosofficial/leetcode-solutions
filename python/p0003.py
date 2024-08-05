class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Initialize pointers for the sliding window and maximum length
        left = right = maximum = 0
        # Set to store unique characters in the current window
        seen = set()

        # Loop until the right pointer reaches the end of the string
        while right < len(s):
            # If the character at the right pointer is not in the set
            if s[right] not in seen:
                # Add the character to the set
                seen.add(s[right])
                # Update the maximum length if the current window is larger
                maximum = max(maximum, right - left + 1)
                # Move the right pointer to expand the window
                right += 1
            else:
                # If the character is in the set, remove the character at the left pointer
                seen.remove(s[left])
                # Move the left pointer to shrink the window
                left += 1
               
        # Return the maximum length of substring found
        return maximum

# Create an instance of the Solution class
solution = Solution()
# Call the method with the input string and print the result
print(solution.lengthOfLongestSubstring("abcabcbb"))
