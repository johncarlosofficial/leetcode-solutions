from typing import List


class Solution:

  def findMedianSortedArrays(self, nums1: List[int],
                             nums2: List[int]) -> float:

    # Calculate the median indices
    median_indices = []
    total_length = len(nums1) + len(nums2)
    if total_length % 2 == 1:
        # If the total length is odd, there's only one median index
        median_indices = [total_length // 2]
    else:
        # If the total length is even, there are two median indices
        median_indices = [total_length // 2 - 1, total_length // 2]
    
    # Initialize pointers and current index
    index1 = 0
    index2 = 0
    current_index = -1
    current_median = None
    
    # Traverse both arrays until reaching the first median index
    while current_index < median_indices[0]:
        if index1 < len(nums1) and index2 < len(nums2):
            if nums1[index1] <= nums2[index2]:
                current_median = nums1[index1]
                index1 += 1
            else:
                current_median = nums2[index2]
                index2 += 1
        elif index1 < len(nums1):
            current_median = nums1[index1]
            index1 += 1
        else:
            current_median = nums2[index2]
            index2 += 1
        current_index += 1
    
    # If there's only one median index, return the current median
    if len(median_indices) == 1:
        return current_median
    else:
        # If there are two median indices, find the next median value
        second_median = None
        if index1 < len(nums1) and index2 < len(nums2):
            if nums1[index1] <= nums2[index2]:
                second_median = nums1[index1]
            else:
                second_median = nums2[index2]
        elif index1 < len(nums1):
            second_median = nums1[index1]
        else:
            second_median = nums2[index2]
        # Return the average of the two median values
        return (current_median + second_median) / 2

# Test case
solution = Solution()
print(solution.findMedianSortedArrays([1, 2], [3, 4]))
