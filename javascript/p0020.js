/**
 * @param {string} s
 * @return {boolean}
 */
export var isValid = function (s) {
  let stack = []; // Keep track of opening parentheses

  for (let i = 0; i < s.length; i++) {
    let char = s[i];

    if (char == "(" || char == "[" || char == "{") {
      stack.push(char); // Push opening parentheses onto the stack
    } else {
      if (stack.length === 0) return false; // No matching opening parenthesis

      let last = stack.pop(); // Pop the last opening parenthesis

      // Check for matching parentheses
      if (
        (char == ")" && last != "(") ||
        (char == "]" && last != "[") ||
        (char == "}" && last != "{")
      ) {
        return false;
      }
    }
  }

  return stack.length === 0; // All parentheses matched
};
