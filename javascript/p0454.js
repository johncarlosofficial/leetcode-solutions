/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @param {number[]} nums3
 * @param {number[]} nums4
 * @return {number}
 */
export var fourSumCount = function (nums1, nums2, nums3, nums4) {
  let ans = 0;

  let hash_map = {};

  for (let i = 0; i < nums1.length; i++) {
    for (let j = 0; j < nums2.length; j++) {
      const temp = nums1[i] + nums2[j];
      if (temp in hash_map) {
        hash_map[temp] += 1;
      } else {
        hash_map[temp] = 1;
      }
    }
  }

  for (let i = 0; i < nums3.length; i++) {
    for (let j = 0; j < nums4.length; j++) {
      const temp = 0 - (nums3[i] + nums4[j]);
      if (temp in hash_map) {
        ans += hash_map[temp];
      }
    }
  }

  return ans;
};
