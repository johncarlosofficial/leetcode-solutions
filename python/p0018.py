class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort();
        ans = [];
        quad = [];

        def kSum(k: int, start: int, target: int):

            if k != 2:
                for i in range(start, len(nums) - k + 1):
                    if i > start and nums[i] == nums[i-1]:
                        continue
                    else:
                        quad.append(nums[i])
                        kSum(k - 1, i + 1, target - nums[i])
                        quad.pop()
                return

            left, right = start, len(nums) - 1

            while left < right:
                if nums[left] + nums[right] > target:
                    right -= 1

                elif nums[left] + nums[right] < target:
                    left += 1

                else:
                    ans.append(quad + [nums[left], nums[right]])
                    left += 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

        kSum(4, 0, target)
        return ans