from typing import List


class Solution:

  def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    intervals = self.bubbleSort(intervals)
    return self.recursive_merge(intervals)

  def recursive_merge(self, intervals):
    i = 0
    ans = []
    while i < len(intervals):
      if (i + 1) < len(intervals):
        if (intervals[i][1] >= intervals[i + 1][0]):
          if (intervals[i][1] <= intervals[i + 1][1]):
            ans.append([intervals[i][0], intervals[i + 1][1]])
          else:
            ans.append([intervals[i][0], intervals[i][1]])
          i += 2
        else:
          ans.append([intervals[i][0], intervals[i][1]])
          i += 1
      else:
        ans.append([intervals[i][0], intervals[i][1]])
        i += 1
    if len(ans) == len(intervals):
      return ans
    else:
      return self.recursive_merge(ans)

  def bubbleSort(self, intervals: List[List[int]]):
    for i in range(len(intervals)):
      swapped = False
      for j in range(0, len(intervals) - i - 1):
        if intervals[j][0] > intervals[j + 1][0]:
          intervals[j], intervals[j + 1] = intervals[j + 1], intervals[j]
          swapped = True
      if not swapped:
        return intervals
    return intervals
