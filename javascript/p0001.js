/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
export var twoSum = function (nums, target) {
  const numIdx = {}; // Initialize an empty hash map

  for (let i = 0; i < nums.length; i++) {
    // Iterate through the array
    const complement = target - nums[i]; // Calculate the complement
    if (complement in numIdx) {
      // Check if the complement exists in the hash map
      return [numIdx[complement], i]; // Return the indices if found
    }
    numIdx[nums[i]] = i; // Store the current number and its index in the hash map
  }
};
