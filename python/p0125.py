class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return False  
            
        if len(s) == 1:
            return True  

        l = 0  # Left pointer
        r = len(s) - 1  # Right pointer

        while l < r:
            if not s[l].isalnum():  # Skip non-alphanumeric characters on the left
                l += 1
                continue

            if not s[r].isalnum():  # Skip non-alphanumeric characters on the right
                r -= 1
                continue

            if s[l].lower() != s[r].lower():  # Check if characters are not equal ignoring case
                return False

            l += 1  
            r -= 1  

        return True 
