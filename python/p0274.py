from typing import List


class Solution:

    def hIndex(self, citations: List[int]) -> int:
        # Sort the list of citations using merge sort
        citations = self.mergeSort(citations)
        max_h = 0  # Maximum h-index found

        for i in range(len(citations)):
            papers = len(citations) - i
            cites = citations[i]

            h = cites if papers > cites else papers

            # Update the maximum h-index
            max_h = max(max_h, h)

        return max_h

    def mergeSort(self, nums: List[int]) -> List[int]:
        # Base case: a single element is already sorted
        if len(nums) == 1:
            return nums

        # Split the list into two halves
        mid = len(nums) // 2
        left = self.mergeSort(nums[:mid])
        right = self.mergeSort(nums[mid:])

        # Merge the two sorted halves
        return self.merge(left, right)

    def merge(self, left: List[int], right: List[int]) -> List[int]:
        sorted_list = []
        i = j = 0

        # Merge elements from left and right lists in sorted order
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                sorted_list.append(left[i])
                i += 1
            else:
                sorted_list.append(right[j])
                j += 1

        # Append remaining elements from the left list, if any
        sorted_list.extend(left[i:])
        # Append remaining elements from the right list, if any
        sorted_list.extend(right[j:])

        return sorted_list
