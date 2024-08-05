/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function (s) {
  // Initialize pointers for the sliding window and maximum length
  let left = 0;
  let right = 0;
  let maximum = 0;

  // Set to store unique characters in the current window
  let seen = new Set();

  // Loop until the right pointer reaches the end of the string
  while (right < s.length) {
    // If the character at the right pointer is not in the set
    if (!seen.has(s[right])) {
      // Add the character to the set
      seen.add(s[right]);
      // Update the maximum length if the current window is larger
      maximum = Math.max(maximum, right - left + 1);
      // Move the right pointer to expand the window
      right++;
    } else {
      // If the character is in the set, remove the character at the left pointer
      seen.delete(s[left]);
      // Move the left pointer to shrink the window
      left++;
    }
  }

  // Return the maximum length of substring found
  return maximum;
};

// Test case
console.log(lengthOfLongestSubstring("abcabcbb"));
