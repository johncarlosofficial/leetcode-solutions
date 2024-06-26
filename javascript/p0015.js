/**
 * @param {number[]} nums
 * @return {number[][]}
 */
export var threeSum = function (nums) {
  const answer = [];
  nums.sort((a, b) => a - b); // Sort the array

  for (let i = 0; i < nums.length - 2; i++) {
    if (i > 0 && nums[i] === nums[i - 1]) {
      // Skip duplicate numbers
      continue;
    }

    let left = i + 1;
    let right = nums.length - 1;

    while (left < right) {
      const sum = nums[i] + nums[left] + nums[right];

      if (sum === 0) {
        answer.push([nums[i], nums[left], nums[right]]);
        // Move left pointer to the right, skipping duplicates
        while (left < right && nums[left] === nums[left + 1]) left++;
        left++;
        // Move right pointer to the left, skipping duplicates
        while (left < right && nums[right] === nums[right - 1]) right--;
        right--;
      } else if (sum < 0) {
        left++; // Increase the sum by moving the left pointer to the right
      } else {
        right--; // Decrease the sum by moving the right pointer to the left
      }
    }
  }

  return answer;
};
