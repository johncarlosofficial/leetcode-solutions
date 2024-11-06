class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        nums_bin = [0] * len(nums)

        for i in range(len(nums)):
            dec_form = nums[i]
            set_bits = 0

            while dec_form > 0:
                remainder = dec_form % 2
                if remainder == 1:
                    set_bits += 1
                dec_form = dec_form // 2

            nums_bin[i] = set_bits
            
        for i in range(len(nums)):
            for j in range(0, len(nums) - i):
                if j + 1 < len(nums):
                    if nums[j] > nums[j+1]:
                        if nums_bin[j] == nums_bin[j+1]:
                            nums[j], nums[j+1] = nums[j+1], nums[j]
                        else:
                            return False

        return True