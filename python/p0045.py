class Solution:
    def jump(self, nums: List[int]) -> int:
        # 'jumps' will store the minimum number of jumps required to reach the last index
        jumps = 0

        # 'current_start' and 'current_end' represent the range of indices we can jump from
        current_start = 0
        current_end = 0

        # We loop until 'current_end' reaches the last index of the array
        while current_end < len(nums) - 1:
            # 'farthest_jump' will track the farthest position we can reach within the current jump
            farthest_jump = 0

            # Iterate over all indices from 'current_start' to 'current_end' to find the farthest jump
            for i in range(current_start, current_end + 1):
                # Update the farthest position we can reach from the current position 'i'
                farthest_jump = max(farthest_jump, nums[i] + i)

            # Increase the number of jumps as we are moving to a new range
            jumps += 1

            # Move 'current_start' to the next range (just beyond the current end)
            current_start = current_end + 1

            # Update 'current_end' to the farthest position we can jump to
            current_end = farthest_jump

        # Return the total number of jumps required
        return jumps
