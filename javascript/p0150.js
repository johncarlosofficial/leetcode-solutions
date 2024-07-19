/**
 * @param {string[]} tokens
 * @return {number}
 */
export var evalRPN = function (tokens) {
  let stack = [];
  const operators = ["+", "-", "*", "/"]; // Set of valid operators

  for (let char of tokens) {
    if (!operators.includes(char)) {
      // Push numbers onto the stack
      stack.push(parseInt(char));
    } else {
      // Pop two numbers for the operator
      let num2 = stack.pop();
      let num1 = stack.pop();

      // Perform the operation and push the result back onto the stack
      if (char == "+") {
        stack.push(num1 + num2);
      } else if (char == "-") {
        stack.push(num1 - num2);
      } else if (char == "*") {
        stack.push(num1 * num2);
      } else {
        // For division, truncate towards zero
        stack.push(Math.trunc(num1 / num2));
      }
    }
  }

  // The result is the only element left in the stack
  return stack[0];
};
