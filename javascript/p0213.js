/**
 * @param {number[]} nums
 * @return {number}
 */
var rob = function (nums) {
  // Edge cases
  if (nums.length === 1) {
    return nums[0];
  }

  if (nums.length === 2) {
    return Math.max(nums[0], nums[1]);
  }

  // Robbing First House (from index 0 to nums.length - 2)
  let previous_house = 0;
  let two_houses_ago = 0;
  let current_max = 0;

  for (let i = 0; i < nums.length - 1; i++) {
    current_max = Math.max(previous_house, two_houses_ago + nums[i]);
    two_houses_ago = previous_house;
    previous_house = current_max;
  }

  let robbing_first_house_max = previous_house;

  // Robbing Second House (from index 1 to nums.length - 1)
  previous_house = 0;
  two_houses_ago = 0;
  current_max = 0;

  for (let i = 1; i < nums.length; i++) {
    current_max = Math.max(previous_house, two_houses_ago + nums[i]);
    two_houses_ago = previous_house;
    previous_house = current_max;
  }

  let robbing_second_house_max = previous_house;

  // Return the maximum of robbing the first house or the second house
  return Math.max(robbing_first_house_max, robbing_second_house_max);
};
