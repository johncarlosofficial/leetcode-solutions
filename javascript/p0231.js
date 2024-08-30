/**
 * Function to check if a number is a power of two.
 * @param {number} n - The number to check.
 * @return {boolean} - Returns true if n is a power of two, otherwise false.
 */
var isPowerOfTwo = function (n) {
  // If n is less than 1, it cannot be a power of two.
  if (n < 1) return false;

  // If n is exactly 1, return true because 1 is 2^0, which is a power of two.
  if (n === 1) {
    return true;
  } else {
    // Check if n is odd by using the modulus operator.
    if (n % 2) {
      // If n is odd, it cannot be a power of two, so return false.
      return false;
    } else {
      // If n is even, divide it by 2 and call the function recursively.
      return isPowerOfTwo(n / 2);
    }
  }
};

console.log(isPowerOfTwo(16)); // true

/**
 * Function to check if a number is a power of two.
 * @param {number} n - The number to check.
 * @return {boolean} - Returns true if n is a power of two, otherwise false.
 */
var isPowerOfTwo2 = function (n) {
  // A number n is a power of two if and only if it is greater than 0
  // and has exactly one bit set in its binary representation.
  return n > 0 && (n & (n - 1)) === 0;
};

console.log(isPowerOfTwo2(16)); // true
