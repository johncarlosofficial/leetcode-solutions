from typing import List


class Solution:

    def commonChars(self, words: List[str]) -> List[str]:
        ans_map = {}  # Frequency map for characters in the first word

        # Initialize ans_map with the first word's characters
        for char in words[0]:
            if char in ans_map:
                ans_map[char] += 1
            else:
                ans_map[char] = 1

        # Compare each subsequent word with ans_map
        for word in words:
            temp_map = {}  # Temporary frequency map for the current word
            for char in word:
                if char in temp_map:
                    temp_map[char] += 1
                else:
                    temp_map[char] = 1

            # Update ans_map with the minimum frequency of each character
            for char in ans_map:
                if char not in temp_map:
                    ans_map[char] = 0
                else:
                    ans_map[char] = min(ans_map[char], temp_map[char])

        # Build the result list from ans_map
        ans = []
        for char in ans_map:
            if ans_map[char] > 0:
                for _ in range(ans_map[char]):
                    ans.append(char)

        return ans
