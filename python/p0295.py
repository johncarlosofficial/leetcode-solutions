from collections import deque


class MedianFinder:

  def __init__(self):
    self.main = deque()
    self.secondary = deque()

  def addNum(self, num: int) -> None:
    if not self.main:
      self.main.append(num)
    else:
      if num >= self.main[-1]:
        self.main.append(num)
      elif num <= self.main[0]:
        self.main.appendleft(num)
      else:
        if num > self.main[len(self.main) // 2]:
          while self.main[-1] > num:
            self.secondary.append(self.main.pop())
          self.main.append(num)
          while self.secondary:
            self.main.append(self.secondary.pop())
        else:
          while self.main[0] < num:
            self.secondary.appendleft(self.main.popleft())
          self.main.appendleft(num)
          while self.secondary:
            self.main.appendleft(self.secondary.popleft())

  def findMedian(self) -> float:
    if len(self.main) % 2:
      return self.main[len(self.main) // 2]
    else:
      average = (self.main[len(self.main) // 2] +
                 self.main[(len(self.main) // 2) - 1]) / 2
      return average
