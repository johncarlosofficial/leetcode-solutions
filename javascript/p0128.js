/**
 * @param {number[]} nums
 * @return {number}
 */
export var longestConsecutive = function (nums) {
  // Create a set from the array
  let hashSet = new Set(nums);
  // Initialize max length
  let maxLength = 0;

  // Iterate through each number in the set
  hashSet.forEach((num) => {
    // Check if it's the start of a sequence
    if (!hashSet.has(num - 1)) {
      let count = 1;
      // Check for the next numbers in the sequence
      while (hashSet.has(num + 1)) {
        count++;
        num++;
      }

      // Update max length if current sequence is longer
      maxLength = Math.max(maxLength, count);
    }
  });

  return maxLength;
};
