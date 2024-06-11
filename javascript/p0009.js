/**
 * @param {number} x
 * @return {boolean}
 */
export var isPalindrome = function (x) {
  if (x < 0) {
    return false;
  }

  let original = x;
  let reversed = 0;

  while (original > 0) {
    let lastDigit = original % 10;
    reversed = reversed * 10 + lastDigit;
    original = Math.floor(original / 10);
  }

  return x === reversed;
};
