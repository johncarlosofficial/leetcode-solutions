from typing import List


class Solution:

  def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
    if n == 0:
      return True

    count = 0
    for i in range(len(flowerbed)):
      if i - 1 < 0 and i + 1 == len(flowerbed):
        if flowerbed[i] == 0:
          flowerbed[i] = 1
          count += 1
          if count == n:
            return True
      elif i - 1 < 0:
        if flowerbed[i] == 0 and flowerbed[i + 1] == 0:
          flowerbed[i] = 1
          count += 1
          if count == n:
            return True
      elif i + 1 == len(flowerbed):
        if flowerbed[i - 1] == 0 and flowerbed[i] == 0:
          flowerbed[i] = 1
          count += 1
          if count == n:
            return True
      else:
        if flowerbed[i - 1] == 0 and flowerbed[i] == 0 and flowerbed[i +
                                                                     1] == 0:
          flowerbed[i] = 1
          count += 1
          if count == n:
            return True

    return False
