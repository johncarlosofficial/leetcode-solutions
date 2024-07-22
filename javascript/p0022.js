/**
 * @param {number} n
 * @return {string[]}
 */
var generateParenthesis = function (n) {
  let ans = []; // To store valid combinations
  let stack = []; // To build the current combination

  function backtrack(opened, closed) {
    // Base case: all parentheses used
    if (opened === closed && opened === n) {
      ans.push(stack.join("")); // Add the current combination
    }

    // Can add an opening bracket
    if (opened < n) {
      stack.push("(");
      backtrack(opened + 1, closed);
      stack.pop();
    }

    // Can add a closing bracket
    if (opened > closed) {
      stack.push(")");
      backtrack(opened, closed + 1);
      stack.pop();
    }
  }

  backtrack(0, 0); // Start the recursion with 0 opened and closed

  return ans; // Return all valid combinations
};
