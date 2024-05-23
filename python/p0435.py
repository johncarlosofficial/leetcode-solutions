from typing import List


class Solution:

    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = self.mergeSort(intervals)

        end = intervals[0][1]
        ans = 0

        for i in range(1, len(intervals)):
            if intervals[i][0] < end:
                if intervals[i][1] < end:
                    end = intervals[i][1]
                ans += 1
            else:
                end = intervals[i][1]

        return ans

    def mergeSort(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1:
            return intervals

        mid = len(intervals) // 2
        left = self.mergeSort(intervals[:mid])
        right = self.mergeSort(intervals[mid:])

        return self.merge(left, right)

    def merge(self, left: List[List[int]],
              right: List[List[int]]) -> List[List[int]]:
        merged = []

        l_idx, r_idx = 0, 0

        while l_idx < len(left) and r_idx < len(right):
            if left[l_idx][0] < right[r_idx][0]:
                merged.append(left[l_idx])
                l_idx += 1
            else:
                merged.append(right[r_idx])
                r_idx += 1

        merged.extend(left[l_idx:])
        merged.extend(right[r_idx:])

        return merged
