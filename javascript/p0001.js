/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    hash_map = {}

    for (let i = 0; i < nums.length; i++) {
        if ((target - nums[i]) in hash_map) {
            return [hash_map[target - nums[i]], i]
        }
        else {
            hash_map[nums[i]] = i
        }
    }

    return []
};