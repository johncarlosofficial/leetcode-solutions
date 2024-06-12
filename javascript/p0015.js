/**
 * @param {number[]} nums
 * @return {number[][]}
 */
export var threeSum = function (nums) {
  const ans = [];
  nums.sort((a, b) => a - b);

  for (let i = 0; i < nums.length - 2; i++) {
    // Skip duplicated elements
    if (i > 0 && nums[i] === nums[i - 1]) {
      continue;
    }

    let left = i + 1;
    let right = nums.length - 1;

    while (left < right) {
      const sum = nums[i] + nums[left] + nums[right];
      if (sum === 0) {
        ans.push([nums[i], nums[left], nums[right]]);

        // Move left and right pointers to the next different elements
        while (left < right && nums[left] === nums[left + 1]) {
          left++;
        }
        while (right > left && nums[right] === nums[right + 1]) {
          right--;
        }
        left++;
        right--;
      } else if (sum < 0) {
        left++;
      } else {
        right--;
      }
    }
  }

  return ans;
};
