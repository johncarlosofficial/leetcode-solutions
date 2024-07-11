/**
 * @param {number[]} height
 * @return {number}
 */
export var trap = function (height) {
  if (height.length === 0) {
    return 0;
  }

  const n = height.length;

  // Initialize arrays to store the maximum height to the left and right of each bar
  const maxLefts = new Array(n).fill(0);
  const maxRights = new Array(n).fill(0);

  // Compute maximum heights to the left of each bar
  maxLefts[0] = height[0];
  for (let i = 1; i < n; i++) {
    maxLefts[i] = Math.max(maxLefts[i - 1], height[i]);
  }

  // Compute maximum heights to the right of each bar
  maxRights[n - 1] = height[n - 1];
  for (let i = n - 2; i >= 0; i--) {
    maxRights[i] = Math.max(maxRights[i + 1], height[i]);
  }

  // Calculate the water trapped at each bar
  let trappedWater = 0;
  for (let i = 0; i < n; i++) {
    const water = Math.min(maxLefts[i], maxRights[i]) - height[i];
    if (water > 0) {
      trappedWater += water;
    }
  }

  return trappedWater;
};
