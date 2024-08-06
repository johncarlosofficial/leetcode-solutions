class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dictionary = {}  # Counts occurrences of characters in the current window
        left = right = 0  # Sliding window pointers
        longest = 0  # Longest substring found

        while right < len(s):
            # Increment count of s[right]
            dictionary[s[right]] = dictionary.get(s[right], 0) + 1  

            # Shrink window if replacements needed exceed k
            while right - left + 1 - max(dictionary.values()) > k:
                dictionary[s[left]] -= 1
                if dictionary[s[left]] == 0:
                    del dictionary[s[left]]
                left += 1

            # Update longest substring length
            longest = max(longest, right - left + 1)  
            right += 1

        return longest

# Test case
solution = Solution()
print(solution.characterReplacement("AABABBA", 1))  # Output should be 4
