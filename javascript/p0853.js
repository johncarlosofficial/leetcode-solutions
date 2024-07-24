/**
 * @param {number} target
 * @param {number[]} position
 * @param {number[]} speed
 * @return {number}
 */
var carFleet = function (target, position, speed) {
  // Array to hold the position and speed pairs
  let ps = [];
  for (let i = 0; i < position.length; i++) {
    ps.push([position[i], speed[i]]);
  }

  // Sort the array based on the car positions in ascending order
  ps.sort((a, b) => a[0] - b[0]);

  // Stack to keep track of car fleets
  let stack = [];
  for (let i = ps.length - 1; i >= 0; i--) {
    if (stack.length === 0) {
      stack.push(ps[i]);
    } else {
      let time1 =
        (target - stack[stack.length - 1][0]) / stack[stack.length - 1][1];
      let time2 = (target - ps[i][0]) / ps[i][1];

      // If the current car takes longer to reach the target, it forms a new fleet
      if (time1 < time2) {
        stack.push(ps[i]);
      }
    }
  }

  // The number of car fleets is the size of the stack
  return stack.length;
};
