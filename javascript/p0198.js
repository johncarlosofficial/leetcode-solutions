/**
 * @param {number[]} nums
 * @return {number}
 */
var rob = function (nums) {
  if (nums.length === 1) {
    return nums[0];
  }

  if (nums.length === 2) {
    return Math.max(nums[0], nums[1]);
  }

  let two_houses_ago = 0;
  let previous_house = 0;

  for (let i = 0; i < nums.length; i++) {
    let current_max = Math.max(nums[i] + two_houses_ago, previous_house);
    two_houses_ago = previous_house;
    previous_house = current_max;
  }

  return previous_house;
};
