from python.p0155 import MinStack

solution = MinStack()
solution.push(1)
solution.push(-5)
solution.push(3)
solution.push(2)

print(solution.getMin())
solution.pop()
print(solution.getMin())
solution.pop()
print(solution.getMin())
solution.pop()
print(solution.getMin())