class Solution:

  def longestConsecutive(self, nums) -> int:
    num_set = set(nums)
    max_length = 0

    for num in num_set:
      # Check if the current number is the start of a sequence
      if num - 1 not in num_set:
        current_num = num
        current_length = 1

        # Expand the current sequence to the right
        while current_num + 1 in num_set:
          current_num += 1
          current_length += 1

        max_length = max(max_length, current_length)

    return max_length
