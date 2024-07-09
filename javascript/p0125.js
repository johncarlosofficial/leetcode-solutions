/**
 * @param {string} s
 * @return {boolean}
 */
export var isPalindrome = function (s) {
  const regex = /^[a-zA-Z0-9]$/; // Regular expression to match alphanumeric characters

  if (!s) return false;
  if (s.length === 1) return true;

  let l = 0; // Left pointer
  let r = s.length - 1; // Right pointer

  while (l < r) {
    if (!regex.test(s[l])) {
      // Skip non-alphanumeric characters on the left
      l += 1;
      continue;
    }

    if (!regex.test(s[r])) {
      // Skip non-alphanumeric characters on the right
      r -= 1;
      continue;
    }

    if (s[l].toLocaleLowerCase() != s[r].toLocaleLowerCase()) return false; // Check if characters are not equal ignoring case

    l += 1;
    r -= 1;
  }

  return true;
};
