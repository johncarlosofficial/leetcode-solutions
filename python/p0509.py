from typing import List

class Solution:
    def fib(self, n: int) -> int:
        # Base cases: if n is 0, return 0, and if n is 1, return 1
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            # Initialize the sequence with the first two Fibonacci numbers
            sequence = [0, 1]
            # Call the helper function to compute the nth Fibonacci number
            return self.seq(sequence, n)

    def seq(self, nums: List[int], n: int) -> int:
        # If the sequence has the required length (n+1 elements), return the last element
        if len(nums) == n + 1:
            return nums[-1]
        else:
            # Append the next Fibonacci number to the sequence
            nums.append(nums[-1] + nums[-2])
            # Recursively call the function to continue building the sequence
            return self.seq(nums, n)

# Test case
solution = Solution()
# Print the 4th Fibonacci number (0-based index, so this should print 3)
print(solution.fib(4))
