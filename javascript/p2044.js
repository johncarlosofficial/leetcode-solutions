/**
 * @param {number[]} nums
 * @return {number}
 */
var countMaxOrSubsets = function (nums) {
  let max_or = 0;

  for (let i = 0; i < nums.length; i++) {
    max_or |= nums[i];
  }

  function backtrack(i, curr_or) {
    if (i == nums.length) {
      return curr_or == max_or ? 1 : 0;
    }

    return (
      // Include nums[i] in the subset
      backtrack(i + 1, curr_or) +
      // Exclude nums[i] from the subset
      backtrack(i + 1, curr_or | nums[i])
    );
  }

  return backtrack(0, 0);
};
