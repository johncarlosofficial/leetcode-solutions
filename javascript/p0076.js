/**
 * @param {string} s
 * @param {string} t
 * @return {string}
 */
var minWindow = function (s, t) {
  // If the source string is shorter than the target string, it's impossible to find a valid window
  if (s.length < t.length) {
    return "";
  }

  // Map to count characters in the target string
  const targetCount = {};
  // Map to count characters in the current window of the source string
  const windowCount = {};

  // Initialize the minimum length of the window as Infinity
  let minWindowLength = Infinity;
  // Initialize the result string for the smallest window found
  let minWindowStr = "";

  // Fill the targetCount map with character counts from the target string
  for (const char of t) {
    if (targetCount[char]) {
      targetCount[char]++;
    } else {
      targetCount[char] = 1;
    }

    // Initialize windowCount map with zeros for characters in target string
    windowCount[char] = 0;
  }

  // Helper function to check if the current window satisfies the target string requirements
  const isValid = () => {
    for (const char in targetCount) {
      if (windowCount[char] < targetCount[char]) {
        return false;
      }
    }
    return true;
  };

  // Start of the current window in the source string
  let left = 0;
  // Iterate through each character in the source string
  for (let right = 0; right < s.length; right++) {
    // Add the current character to the windowCount if it's part of the target string
    if (windowCount.hasOwnProperty(s[right])) {
      windowCount[s[right]]++;
    }

    // Shrink the window from the left as long as the window is valid
    while (isValid()) {
      // Update the result with the smallest valid window found
      if (right - left + 1 < minWindowLength) {
        minWindowLength = right - left + 1;
        minWindowStr = s.substring(left, right + 1);
      }

      // Remove the character at the left end of the window from windowCount
      if (windowCount.hasOwnProperty(s[left])) {
        windowCount[s[left]]--;
      }

      // Move the left end of the window to the right
      left++;
    }
  }

  return minWindowStr;
};

// Exemple usage
console.log(minWindow("ADOBECODEBANC", "ABC"));
