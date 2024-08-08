class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # If the source string is shorter than the target string, it's impossible to find a valid window
        if len(s) < len(t):
            return ""

        # Dictionary to count characters in the target string
        target_count = {}
        # Dictionary to count characters in the current window of the source string
        window_count = {}

        # Initialize the minimum length of the window as infinity
        min_window_length = float("infinity")
        # Initialize the result string for the smallest window found
        min_window_str = ""

        # Fill the target_count dictionary with character counts from target string
        for char in t:
            if char in target_count:
                target_count[char] += 1
            else:
                target_count[char] = 1

            # Initialize window_count dictionary with zeros for characters in target string
            window_count[char] = 0

        # Helper function to check if the current window satisfies the target string requirements
        def isValid() -> bool:
            for char in target_count:
                if window_count[char] < target_count[char]:
                    return False
            return True

        # Start of the current window in the source string
        left = 0
        # Iterate through each character in the source string
        for right in range(len(s)):
            # Add the current character to the window_count if it's part of the target string
            if s[right] in window_count:
                window_count[s[right]] += 1

            # Shrink the window from the left as long as the window is valid
            while isValid():
                # Update the result with the smallest valid window found
                if right - left + 1 < min_window_length:
                    min_window_length = right - left + 1
                    min_window_str = s[left:right+1]

                # Remove the character at the left end of the window from window_count
                if s[left] in window_count:
                    window_count[s[left]] -= 1

                # Move the left end of the window to the right
                left += 1

        return min_window_str

# Example usage
solution = Solution()
print(solution.minWindow("ADOBECODEBANC", "ABC"))