/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
export var twoSum = function (nums, target) {
  let num_idx = {};

  for (let i = 0; i < nums.length; i++) {
    let complement = target - nums[i];
    if (complement in num_idx) {
      return [num_idx[complement], i];
    } else {
      num_idx[nums[i]] = i;
    }
  }
};
