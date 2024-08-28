/**
 * Computes the nth Fibonacci number.
 * @param {number} n - The index of the Fibonacci number to compute.
 * @return {number} - The nth Fibonacci number.
 */
var fib = function (n) {
  // Base cases: if n is 0, return 0; if n is 1, return 1
  if (n === 0) return 0;
  else if (n === 1) return 1;
  else {
    // Initialize the array with the first two Fibonacci numbers
    let nums = [0, 1];
    // Call the helper function to compute the nth Fibonacci number
    return seq(nums, n);
  }
};

/**
 * Helper function to build the Fibonacci sequence recursively.
 * @param {number[]} nums - The current Fibonacci sequence.
 * @param {number} n - The index of the Fibonacci number to compute.
 * @return {number} - The nth Fibonacci number.
 */
var seq = function (nums, n) {
  // If the array has the required length (n+1 elements), return the last element
  if (nums.length === n + 1) return nums[nums.length - 1];
  else {
    // Compute the next Fibonacci number and add it to the array
    nums.push(nums[nums.length - 1] + nums[nums.length - 2]);
    // Recursively call the function to continue building the sequence
    return seq(nums, n);
  }
};

// Test case
console.log(fib(4)); // Prints the 4th Fibonacci number (0-based index, so this should print 3)
