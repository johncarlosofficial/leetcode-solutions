/**
 * @param {number[]} nums
 * @return {number}
 */
export var findDuplicate = function (nums) {
  // Initialize the pointers for cycle detection
  let slow = nums[0];
  let fast = nums[0];

  // Move slow pointer by one step and fast pointer by two steps until they meet
  do {
    slow = nums[slow];
    fast = nums[nums[fast]];
  } while (slow != fast);

  // Move one pointer to the start and find the cycle entry point
  slow = nums[0];
  while (slow != fast) {
    slow = nums[slow];
    fast = nums[fast];
  }

  return slow;
};
