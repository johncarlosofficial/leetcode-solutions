from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Stack to keep track of temperatures and their indices
        temp_stack = [] 
        # Answer list initialized with zeros, same length as temperatures list
        days_to_wait = [0] * len(temperatures)
        
        for current_day, current_temp in enumerate(temperatures):
            # Check if the current temperature is higher than the temperature at the top of the stack
            while temp_stack and current_temp > temp_stack[-1][0]:
                # Pop the top element from the stack (it's now warmer)
                previous_temp, previous_day = temp_stack.pop()
                # Calculate the number of days to wait for a warmer temperature
                days_to_wait[previous_day] = current_day - previous_day 
            # Push the current temperature and its index onto the stack
            temp_stack.append([current_temp, current_day])
                
        return days_to_wait


solution = Solution()
print(solution.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
