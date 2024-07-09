/**
 * @param {number[]} numbers
 * @param {number} target
 * @return {number[]}
 */
export var twoSum = function (numbers, target) {
  let l = 0; // Left pointer
  let r = numbers.length - 1; // Right pointer

  while (l < r) {
    const temp = numbers[l] + numbers[r]; // Sum of the numbers at left and right pointers
    if (temp == target) return [l + 1, r + 1]; // Return 1-based indices if sum matches target
    temp < target ? (l += 1) : (r -= 1); // Move pointers based on comparison with target
  }
};
