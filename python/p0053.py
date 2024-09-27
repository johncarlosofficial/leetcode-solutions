class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Initialize two variables:
        # max_sum will store the maximum sum we've found so far, 
        # starting with the first element of the array.
        # current_sum keeps track of the sum of the current subarray we're exploring.
        max_sum = current_sum = nums[0]

        # Iterate over the array starting from the second element
        for i in range(1, len(nums)):
            # For each element, decide whether to:
            # 1. Start a new subarray with the current element (nums[i])
            # 2. Add the current element to the previous subarray (nums[i] + current_sum)
            # Take the maximum of the two and update current_sum.
            current_sum = max(nums[i], nums[i] + current_sum)
            
            # Update max_sum if the current_sum is greater than the max_sum we've seen so far.
            max_sum = max(max_sum, current_sum)

        # After iterating through the array, max_sum will hold the largest sum of any subarray.
        return max_sum
