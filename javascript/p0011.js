/**
 * @param {number[]}
 * @return {number}
 */
export var maxArea = function (height) {
  let l = 0; // Left pointer
  let r = height.length - 1; // Right pointer
  let ans = 0; // Maximum area

  while (l < r) {
    // Calculate the current water area
    const water = (r - l) * Math.min(height[l], height[r]);
    // Update the maximum area if current is larger
    ans = Math.max(ans, water);

    // Move the pointer with the shorter line inward
    if (height[l] < height[r]) {
      l += 1;
    } else {
      r -= 1;
    }
  }

  return ans; // Return the maximum area found
};
