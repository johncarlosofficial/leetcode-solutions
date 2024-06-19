from typing import List

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        ans = 0

        pre_sums = {}

        for i in range(len(nums1)):
            for j in range(len(nums2)):
                temp = nums1[i] + nums2[j]

                if temp in pre_sums:
                    pre_sums[temp] += 1
                else:
                    pre_sums[temp] = 1
                
                
        for k in range(len(nums3)):
            for p in range(len(nums4)):
                temp = 0 - (nums3[k] + nums4[p])

                if temp in pre_sums:
                    ans += pre_sums[temp]

        return ans

