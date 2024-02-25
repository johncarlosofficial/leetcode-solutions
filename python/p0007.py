class Solution:

  def reverse(self, x: int) -> int:
    num = list(str(x))
    if num[0] == '-':
      left = 1
      right = len(num) - 1
      while left < right:
        num[left], num[right] = num[right], num[left]
        right -= 1
        left += 1
      ans = int(''.join(num))
      return ans if ans >= -2**31 else 0
    else:
      left = 0
      right = len(num) - 1
      while left < right:
        num[left], num[right] = num[right], num[left]
        right -= 1
        left += 1
      ans = int(''.join(num))
      return ans if ans <= 2**31 - 1 else 0
