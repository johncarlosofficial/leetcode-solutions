/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var maxSlidingWindow = function (nums, k) {
  const ans = []; // Stores the max of each window
  const maxToMin = []; // Deque to keep track of max elements

  let left = 0,
    right = 0; // Window pointers

  // Process the first window
  while (right < k) {
    while (maxToMin.length && maxToMin[maxToMin.length - 1] < nums[right]) {
      maxToMin.pop(); // Maintain decreasing order in deque
    }
    maxToMin.push(nums[right]);
    right++;
  }

  ans.push(maxToMin[0]); // First window max

  // Process the rest of the windows
  while (right < nums.length) {
    if (maxToMin[0] === nums[left]) {
      maxToMin.shift(); // Remove element leaving the window
    }
    while (maxToMin.length && maxToMin[maxToMin.length - 1] < nums[right]) {
      maxToMin.pop();
    }
    maxToMin.push(nums[right]);
    ans.push(maxToMin[0]); // Current window max
    left++;
    right++;
  }

  return ans; // Return all window maximums
};

// Exemple usage
console.log(maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3));
