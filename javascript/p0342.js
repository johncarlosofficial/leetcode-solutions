/**
 * @param {number} n
 * @return {boolean}
 */
var isPowerOfFour = function (n) {
  // Check if n is less than 1. If so, it can't be a power of four.
  if (n < 1) {
    return false;
  }

  // If n is exactly 1, return true because 1 is 4^0, which is a power of four.
  if (n === 1) {
    return true;
  }

  // Otherwise, check if n is divisible by four.
  if (n % 4 === 0) {
    // If n is divisible by four, divide it by 4 and call the function recursively.
    return isPowerOfFour(n / 4);
  } else {
    // Otherwise, it can't be a power of four.
    return false;
  }
};

console.log(isPowerOfFour(16));

var isPowerOfFour2 = function (n) {
  // Check if n is positive and a power of two
  // (n > 0): Ensure the number is positive
  // (n & (n - 1)) === 0: Check if n is a power of two
  // (n - 1) % 3 === 0: Check if the power of two is a power of four
  return n > 0 && (n & (n - 1)) === 0 && (n - 1) % 3 === 0;
};

console.log(isPowerOfFour2(16));
