class Solution:

  def romanToInt(self, s: str) -> int:
    hash_map = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    nums = []

    for char in s:
      nums.append(hash_map[char])

    ans = 0
    left, right = 0, 1

    while right < len(nums) and left < len(nums):
      if nums[left] >= nums[right]:
        ans += nums[left]
        right += 1
        left += 1
      else:
        ans += (nums[right] - nums[left])
        right += 2
        left += 2

    if left < len(nums):
      ans += nums[left]

    if right < len(nums):
      ans += nums[right]

    return ans
