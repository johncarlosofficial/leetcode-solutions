class MinStack:
    def __init__(self):
        self.stack = []  # Main stack to store elements
        self.min = []    # Stack to keep track of minimums

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min or val <= self.min[-1]:
            self.min.append(val)  # Update min stack

    def pop(self) -> None:
        if self.stack:
            if self.stack[-1] == self.min[-1]:
                self.min.pop()  # Remove from min stack if it's the min value
            self.stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]  # Return top element of the main stack

    def getMin(self) -> int:
        if self.min:
            return self.min[-1]  # Return the current minimum


# Example usage:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
