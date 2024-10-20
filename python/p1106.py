class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        # Initialize an empty stack to help evaluate the expression
        stack = []

        # Loop through each character in the boolean expression
        for char in expression:
            # Ignore commas since they are just separators
            if char == ",":
                continue
            # If a closing parenthesis is found, it indicates the end of an expression
            elif char == ")":
                # Initialize flags to track if there are any true or false values inside the current expression
                has_true = has_false = False

                # Pop elements from the stack until the opening parenthesis "(" is found
                while stack[-1] != "(":
                    top = stack.pop()
                    # Set the flag if we encounter a 't' (true) or 'f' (false)
                    if top == "t":
                        has_true = True
                    else:
                        has_false = True
                
                # Remove the opening parenthesis from the stack
                stack.pop()

                # The next element in the stack will be the operator ('!', '&', or '|')
                operator = stack.pop()

                # Evaluate the expression based on the operator
                if operator == "!":
                    # '!' (NOT) negates the value: if the value is true, it becomes false, and vice versa
                    stack.append("t") if not has_true else stack.append("f")
                
                elif operator == "&":
                    # '&' (AND) is true only if all values inside the parentheses are true
                    stack.append("t") if not has_false else stack.append("f")

                else:
                    # '|' (OR) is true if any of the values inside the parentheses are true
                    stack.append("t") if has_true else stack.append("f")
            else:
                # If the character is not a parenthesis or comma, it must be part of the expression ('t', 'f', '!', '&', '|', or '(')
                stack.append(char)

        # The result of the entire expression is at the top of the stack, return True if it's 't' (true), otherwise False
        return stack[-1] == "t"
