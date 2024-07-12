class Solution:
    def isValid(self, s: str) -> bool:
        stack = []  # Stack to keep track of opening parentheses

        for char in s:
            if char in "({[":
                stack.append(char)  # Push opening parentheses onto the stack
            else:
                if not stack:
                    return False  # No matching opening parenthesis

                last = stack.pop()  # Pop the last opening parenthesis

                # Check for matching parentheses
                if (char == ")" and last != "(") or \
                (char == "]" and last != "[") or \
                (char == "}" and last != "{"):
                    return False

        return not stack  # All parentheses matched