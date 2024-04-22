from typing import List


class Solution:

  def kidsWithCandies(self, candies: List[int],
                      extraCandies: int) -> List[bool]:
    greatest = candies[0]
    ans = [False] * len(candies)

    for i in range(1, len(candies)):
      greatest = max(greatest, candies[i])

    for i in range(len(candies)):
      if candies[i] + extraCandies >= greatest:
        ans[i] = True

    return ans
