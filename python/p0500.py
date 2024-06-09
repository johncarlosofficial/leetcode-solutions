from typing import List


class Solution:

    def findWords(self, words: List[str]) -> List[str]:
        row1 = {"q", "w", "e", "r", "t", "y", "u", "i", "o", "p"}
        row2 = {"a", "s", "d", "f", "g", "h", "j", "k", "l"}
        row3 = {"z", "x", "c", "v", "b", "n", "m"}

        ans = []

        for word in words:
            if word[0].lower() in row1:
                if self.checkUniqueness(word, row1):
                    ans.append(word)

            elif word[0].lower() in row2:
                if self.checkUniqueness(word, row2):
                    ans.append(word)

            else:
                if self.checkUniqueness(word, row3):
                    ans.append(word)

        return ans

    def checkUniqueness(self, word: str, row: set) -> bool:
        passed = True

        for i in range(1, len(word)):
            if word[i].lower() not in row:
                passed = False

        return passed
