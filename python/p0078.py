from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def recursion(idx: int, subset: List[int]):
            # Add a copy of the current subset to the answer list
            ans.append(subset[:])

            # Iterate over the elements starting from the current index
            for i in range(idx, len(nums)):
                # Add the current element to the subset
                subset.append(nums[i])
                # Recur with the next index to continue building the subset
                recursion(i + 1, subset)
                # Remove the last added element (backtracking)
                subset.pop()

        recursion(0, [])
        return ans