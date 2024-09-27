/**
 * @param {number[]} nums - An array of numbers
 * @return {number} - The maximum sum of any contiguous subarray
 */
var maxSubArray = function (nums) {
  // Initialize two variables:
  // maxSum will store the maximum sum we've found so far, starting with the first element.
  // currentSum keeps track of the sum of the current subarray we're exploring.
  let maxSum = nums[0];
  let currentSum = nums[0];

  // Iterate over the array starting from the second element
  for (let i = 1; i < nums.length; i++) {
    // For each element, decide whether to:
    // 1. Start a new subarray with the current element (nums[i])
    // 2. Add the current element to the previous subarray (currentSum + nums[i])
    // Take the maximum of the two and update currentSum.
    currentSum = Math.max(nums[i], currentSum + nums[i]);

    // Update maxSum if currentSum is greater than the maxSum we've seen so far.
    maxSum = Math.max(maxSum, currentSum);
  }

  // After iterating through the array, maxSum will hold the largest sum of any subarray.
  return maxSum;
};
