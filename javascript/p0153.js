/**
 * @param {number[]} nums
 * @return {number}
 */
var findMin = function (nums) {
  let left = 0;
  let right = nums.length - 1;

  while (left < right) {
    const mid = Math.floor((left + right) / 2);
    // If the middle element is greater than the rightmost element,
    // the smallest value must be in the right half
    if (nums[mid] > nums[right]) {
      left = mid + 1;
    }
    // If the middle element is less than or equal to the rightmost element,
    // the smallest value is in the left half (including middle)
    else {
      right = mid;
    }
  }

  // After the loop, left == right and it
  // should point to the smallest element
  return nums[left];
};
