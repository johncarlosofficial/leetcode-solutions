/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
export var subarraySum = function (nums, k) {
  let hash_map = {};
  let prefix = 0;
  let ans = 0;

  for (let i = 0; i < nums.length; i++) {
    prefix += nums[i];

    if (prefix === k) {
      ans += 1;
    }

    if (prefix - k in hash_map) {
      ans += hash_map[prefix - k];
    }

    if (prefix in hash_map) {
      hash_map[prefix] += 1;
    } else {
      hash_map[prefix] = 1;
    }
  }

  return ans;
};
