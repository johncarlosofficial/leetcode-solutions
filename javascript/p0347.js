/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
export var topKFrequent = function (nums, k) {
  const numFreq = {};

  // Count the frequency of each number
  for (const num of nums) {
    if (num in numFreq) {
      numFreq[num] += 1;
    } else {
      numFreq[num] = 1;
    }
  }

  // Create an array of empty arrays to store numbers by their frequency
  const frequencies = Array.from({ length: nums.length + 1 }, () => []);

  // Populate the frequencies array
  for (const num in numFreq) {
    const freq = numFreq[num];
    frequencies[freq].push(parseInt(num));
  }

  const ans = [];
  let counter = 0;

  // Iterate from the highest frequency to the lowest
  for (let i = frequencies.length - 1; i >= 0; i--) {
    if (frequencies[i].length === 0) {
      continue;
    }
    for (const num of frequencies[i]) {
      ans.push(num);
      counter += 1;

      if (counter >= k) {
        return ans;
      }
    }
  }

  return ans;
};
