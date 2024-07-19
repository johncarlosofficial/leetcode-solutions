from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {"+", "-", "*", "/"}  # Set of valid operators
        
        for char in tokens:
            if char not in operators:
                # Push numbers onto the stack
                stack.append(int(char))
            else:
                # Pop two numbers for the operator
                num2 = stack.pop()
                num1 = stack.pop()
                
                # Perform the operation and push the result back onto the stack
                if char == "+":
                    stack.append(num1 + num2)
                elif char == "-":
                    stack.append(num1 - num2)
                elif char == "*":
                    stack.append(num1 * num2)
                else:
                    # For division, truncate towards zero
                    stack.append(int(num1 / num2))
                    
        return stack[0]  # The result is the only element left in the stack
