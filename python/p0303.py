from typing import List


class NumArray:

  def __init__(self, nums: List[int]):
    self.nums = []
    prefix_sum = 0
    for i in range(len(nums)):
      prefix_sum += nums[i]
      self.nums.append(prefix_sum)

  def sumRange(self, left: int, right: int) -> int:
    if left > 0:
      return self.nums[right] - self.nums[left - 1]
    else:
      return self.nums[right]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
