class Solution:

  def myPow(self, x: float, n: int) -> float:
    if n == 0:
      return 1
    if x == 0:
      return 0
    if n < 0:
      x = 1 / x
      n = -n
    return self.pow_recursive(x, n)

  def pow_recursive(self, x, n):
    if n == 1:
      return x
    if n % 2 == 0:
      return self.pow_recursive(x * x, n // 2)
    else:
      return x * self.pow_recursive(x * x, (n - 1) // 2)
