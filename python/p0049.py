from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for word in strs:
            temp = []
            for char in word:
                temp.append(char)
            temp.sort()
            temp = "".join(temp)
            if temp in groups:
                groups[temp].append(word)
            else:
                groups[temp] = [word]

        return list(groups.values())