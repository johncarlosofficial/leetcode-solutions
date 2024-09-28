/**
 * @param {number} n
 * @return {number}
 */
var climbStairs = function (n) {
  // If there is only 1 step, there is only 1 way to climb the staircase.
  if (n === 1) {
    return 1;
  }

  // If there are 2 steps, there are 2 ways to climb (1 step + 1 step, or 2 steps).
  if (n === 2) {
    return 2;
  }

  // Variable to store the number of ways to reach the (n-2)th step.
  let waysToClimbTwoStepsBefore = 1;

  // Variable to store the number of ways to reach the (n-1)th step.
  let waysToClimbOneStepBefore = 2;

  // Variable to store the total number of ways to climb the staircase for the current step.
  let totalWaysToClimb = 0;

  // Loop through from step 3 to n to calculate the number of ways to reach each step.
  for (let step = 3; step <= n; step++) {
    // The total number of ways to reach the current step is the sum of:
    // 1. The number of ways to reach the previous step (n-1).
    // 2. The number of ways to reach the step before that (n-2).
    totalWaysToClimb = waysToClimbOneStepBefore + waysToClimbTwoStepsBefore;

    // Update the values for the next iteration.
    waysToClimbTwoStepsBefore = waysToClimbOneStepBefore;
    waysToClimbOneStepBefore = totalWaysToClimb;
  }

  // Return the total number of ways to reach the nth step.
  return totalWaysToClimb;
};
