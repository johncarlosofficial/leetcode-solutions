/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
export var threeSumClosest = function (nums, target) {
  nums.sort((a, b) => a - b);
  let ans = nums[0] + nums[1] + nums[2];

  for (let i = 0; i < nums.length - 2; i++) {
    let left = i + 1;
    let right = nums.length - 1;

    while (left < right) {
      const tempSum = nums[i] + nums[left] + nums[right];
      if (Math.abs(target - ans) > Math.abs(target - tempSum)) {
        ans = tempSum;
      }

      if (tempSum === target) {
        return tempSum;
      } else if (tempSum < target) {
        left += 1;
      } else {
        right -= 1;
      }
    }
  }

  return ans;
};
