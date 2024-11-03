class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if s == goal:
            return True
            
        rotated = s

        for i in range(len(s)):
            rotated = rotated[1:] + rotated[0]
            if rotated == goal:
                return True

        return False
        