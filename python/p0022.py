from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = [] # To store valid combinations
        stack = [] # To build the current combination

        def backtrack(opened, closed):
            if opened == closed == n: # Base case: all parentheses used
                ans.append("".join(stack)) # Add the current combination
                return

            if opened < n: # Can add an opening bracket
                stack.append("(")  
                backtrack(opened + 1, closed)  
                stack.pop()

            if opened > closed: # Can add a closing bracket
                stack.append(")")
                backtrack(opened, closed + 1)
                stack.pop()

        backtrack(0, 0) # Start the recursion with 0 opened and closed

        return ans # Return all valid combinations
