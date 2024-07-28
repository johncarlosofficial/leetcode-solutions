/**
 * @param {number[]} piles
 * @param {number} h
 * @return {number}
 */
var minEatingSpeed = function (piles, h) {
  // Initialize variables for the maximum and minimum possible eating speeds (bananas per hour)
  let maxEatingSpeed = Math.max(...piles);
  let minEatingSpeed = 1;

  // Initialize the answer with the maximum eating speed
  let optimalSpeed = maxEatingSpeed;

  // Define the search range for binary search
  let left = minEatingSpeed;
  let right = maxEatingSpeed;

  // Perform binary search to find the minimum feasible eating speed
  while (left <= right) {
    let mid = Math.floor((left + right) / 2); // Calculate the mid-point speed
    let totalHours = 0; // Initialize the total hours needed at this speed

    // Calculate the total hours needed to eat all bananas at the current mid-point speed
    for (let pile of piles) {
      if (pile % mid !== 0) {
        // If there are leftover bananas when divided by mid
        totalHours += Math.floor(pile / mid) + 1;
      } else {
        totalHours += pile / mid;
      }
    }

    // Check if the current speed can eat all bananas within the allowed hours
    if (totalHours <= h) {
      optimalSpeed = mid; // Update the optimal speed
      right = mid - 1; // Try to find a lower feasible speed
    } else {
      left = mid + 1; // Increase the speed to reduce total hours
    }
  }

  return optimalSpeed;
};

// Test case
console.log(minEatingSpeed([3, 6, 7, 11], 8));
