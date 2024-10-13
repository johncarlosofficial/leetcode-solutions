import heapq
from typing import List

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        
        # Step 1: Initialize the min-heap and the initial maximum value
        min_heap = []
        max_value = float('-inf')  # Keeps track of the largest element
        
        # Step 2: Push the first element of each list into the heap
        for i in range(len(nums)):
            # Push a tuple (value, list_index, element_index)
            heapq.heappush(min_heap, (nums[i][0], i, 0))
            # Track the maximum value among the current elements
            max_value = max(max_value, nums[i][0])
        
        # Initialize the range to be as large as possible
        range_start, range_end = float('-inf'), float('inf')
        
        # Step 3: Process the heap until we exhaust one of the lists
        while min_heap:
            # Pop the smallest element (min_value, list_index, element_index)
            min_value, list_index, element_index = heapq.heappop(min_heap)
            
            # Check if the current range is smaller than the best range so far
            if max_value - min_value < range_end - range_start:
                range_start, range_end = min_value, max_value
            
            # If we've reached the end of one of the lists, stop
            if element_index + 1 == len(nums[list_index]):
                break
            
            # Otherwise, add the next element from the same list to the heap
            next_value = nums[list_index][element_index + 1]
            heapq.heappush(min_heap, (next_value, list_index, element_index + 1))
            
            # Update the maximum value by comparing the new element with current max_value
            max_value = max(max_value, next_value)

        # Return the smallest range found
        return [range_start, range_end]