from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}

        def recursion(i):
            if i >= len(cost):
                return 0
            
            curr_step = cost[i] if i >= 0 else 0

            one_step, two_steps = 0, 0

            if (i+1) in memo:
                one_step = memo[i+1]
            else:
                memo[i+1] = recursion(i+1)
                one_step = memo[i+1]

            if (i+2) in memo:
                two_steps = memo[i+2]
            else:
                memo[i+2] = recursion(i+2)
                two_steps = memo[i+2]

            return curr_step + min(one_step, two_steps)

        return recursion(-1)
