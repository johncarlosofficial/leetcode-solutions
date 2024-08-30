/**
 * @param {number} n
 * @return {boolean}
 */
var isPowerOfThree = function (n) {
  // Check if n is less than 1. If so, it can't be a power of three.
  if (n < 1) {
    return false;
  }

  // If n is exactly 1, return True because 1 is 3^0, which is a power of three.
  if (n === 1) {
    return true;
  }

  // Otherwise, check if n is divisible by 3.
  if (n % 3 === 0) {
    // If it is, divide it by 3 and call the function recursively.
    return isPowerOfThree(n / 3);
  } else {
    // If it is not, it can't be a power of three.
    return false;
  }
};

/**
 * @param {number} n
 * @return {boolean}
 */
var isPowerOfThree2 = function (n) {
  // 1162261467 is 3^19, the largest power of 3 that fits in a 32-bit integer
  return n > 0 && 1162261467 % n === 0;
};
