/**
 * @param {number[][]} matrix
 * @param {number} target
 * @return {boolean}
 */
var searchMatrix = function (matrix, target) {
  let top = 0;
  let bottom = matrix.length - 1;

  // Binary search to find the correct row
  while (top < bottom) {
    let mid = Math.floor((top + bottom) / 2);

    if (matrix[mid][0] === target) {
      return true;
    } else if (matrix[mid][0] < target) {
      if (matrix[mid][matrix[mid].length - 1] >= target) {
        top = mid;
        bottom = mid;
      } else {
        top = mid + 1;
      }
    } else {
      bottom = mid - 1;
    }
  }

  // Binary search within the row to find the target
  let left = 0;
  let right = matrix[top].length - 1;

  while (left <= right) {
    let mid = Math.floor((left + right) / 2);

    if (matrix[top][mid] === target) {
      return true;
    } else if (matrix[top][mid] < target) {
      left = mid + 1;
    } else {
      right = mid - 1;
    }
  }

  return false; // Return false if the target is not found
};
