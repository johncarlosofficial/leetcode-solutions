class Solution:
    def climbStairs(self, n: int) -> int:
        # If there is only 1 step, there is only 1 way to climb the staircase.
        if n == 1:
            return 1
        
        # If there are 2 steps, there are 2 ways to climb (1 step + 1 step, or 2 steps).
        if n == 2:
            return 2
        
        # Variable to store the number of ways to reach the (n-2)th step.
        waysToClimbTwoStepsBefore = 1
        
        # Variable to store the number of ways to reach the (n-1)th step.
        waysToClimbOneStepBefore = 2
        
        # Variable to store the total number of ways to climb the staircase for the current step.
        totalWaysToClimb = 0
        
        # Loop through from step 3 to n to calculate the number of ways to reach each step.
        for step in range(3, n + 1):
            # The total number of ways to reach the current step is the sum of:
            # 1. The number of ways to reach the previous step (n-1).
            # 2. The number of ways to reach the step before that (n-2).
            totalWaysToClimb = waysToClimbOneStepBefore + waysToClimbTwoStepsBefore
            
            # Update the values for the next iteration.
            waysToClimbTwoStepsBefore = waysToClimbOneStepBefore
            waysToClimbOneStepBefore = totalWaysToClimb
        
        # Return the total number of ways to reach the nth step.
        return totalWaysToClimb
    
class Solution1:
    def climbStairs(self, n: int) -> int:
        # Base case 1: If there are no steps left to climb (n == 0),
        # there's exactly one way to do nothing and stay at the top.
        if n == 0:
            return 1
        
        # Base case 2: If n is negative, it means we've taken an invalid
        # number of steps. There are no valid ways in this case.
        if n < 0:
            return 0
        
        # Recursive case: The total number of ways to climb `n` steps is the sum of:
        # 1. The number of ways to climb the remaining `n-1` steps after taking a single step.
        # 2. The number of ways to climb the remaining `n-2` steps after taking a double step.
        return self.climbStairs(n-1) + self.climbStairs(n-2)
    

class Solution2:
    def climbStairs(self, n: int) -> int:
        if n == 0: 
            return 1
        elif n == 1: 
            return 1
        
        # Memoization dictionary
        memo = {0: 1, 1: 1}
        
        def recursive(n):
            # If already calculated, return the value from the memo
            if n in memo:
                return memo[n]
            
            # Recursively compute the number of ways to climb to the nth step
            memo[n] = recursive(n - 1) + recursive(n - 2)
            return memo[n]
        
        return recursive(n)
