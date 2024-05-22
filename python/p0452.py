from typing import List


class Solution:

    def merge_sort(self, points: List[List[int]]) -> List[List[int]]:
        if len(points) <= 1:
            return points

        mid = len(points) // 2
        left_half = self.merge_sort(points[:mid])
        right_half = self.merge_sort(points[mid:])

        return self.merge(left_half, right_half)

    def merge(self, left: List[List[int]],
              right: List[List[int]]) -> List[List[int]]:
        merged = []
        left_ptr = right_ptr = 0

        while left_ptr < len(left) and right_ptr < len(right):
            if left[left_ptr][0] < right[right_ptr][0]:
                merged.append(left[left_ptr])
                left_ptr += 1
            else:
                merged.append(right[right_ptr])
                right_ptr += 1

        merged.extend(left[left_ptr:])
        merged.extend(right[right_ptr:])
        return merged

    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0

        points_sorted = self.merge_sort(points)

        merged = [points_sorted[0]]
        for i in range(1, len(points_sorted)):
            if points_sorted[i][0] <= merged[-1][1]:
                merged[-1][1] = min(merged[-1][1], points_sorted[i][1])
            else:
                merged.append(points_sorted[i])

        return len(merged)
