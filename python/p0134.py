from typing import List


class Solution:

  def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
    # Calculate differences
    diff = []
    for i in range(len(gas)):
      diff.append(gas[i] - cost[i])

    # Start, sum of past negative gas, and current tank
    start = 0
    past_sum = 0
    tank = 0

    for i in range(len(diff)):
      tank += diff[i]  # Add difference to tank.

      # If tank becomes negative, update past_sum, reset tank, and update start.
      if tank < 0:
        past_sum += tank
        tank = 0
        start = i + 1  # Update start to next station.

    # Check if remaining gas is enough to cover negative gas sum
    if tank >= abs(past_sum):
      return start
    else:
      return -1
