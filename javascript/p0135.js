/**
 * @param {number[]} ratings
 * @return {number}
 */
var candy = function (ratings) {
  // If there's only one child, return 1 candy
  if (ratings.length === 1) {
    return 1;
  }

  // Initialize an array `candies` where each child starts with 1 candy
  let candies = new Array(ratings.length).fill(1);

  // First pass: Left to right
  // If the current child has a higher rating than the previous child,
  // give them more candies than the previous child
  for (let i = 1; i < ratings.length; i++) {
    if (ratings[i] > ratings[i - 1]) {
      candies[i] = candies[i - 1] + 1;
    }
  }

  // Second pass: Right to left
  // If the current child has a higher rating than the next child,
  // make sure they have more candies than the next child
  for (let i = ratings.length - 2; i >= 0; i--) {
    if (ratings[i] > ratings[i + 1]) {
      candies[i] = Math.max(candies[i], candies[i + 1] + 1);
    }
  }

  // The total number of candies needed is the sum of the `candies` array
  return candies.reduce((sum, candy) => sum + candy, 0);
};
