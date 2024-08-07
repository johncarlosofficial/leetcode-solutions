/**
 * @param {string} s1
 * @param {string} s2
 * @return {boolean}
 */
var checkInclusion = function (s1, s2) {
  // If s1 is longer than s2, s1 can't be a permutation of any substring of s2
  if (s1.length > s2.length) {
    return false;
  }

  // Create frequency count arrays for characters in s1 and the current window in s2
  const map1 = new Array(26).fill(0); // Frequency count for s1
  const map2 = new Array(26).fill(0); // Frequency count for the current window in s2

  // Populate map1 with the frequency of each character in s1
  for (const char of s1) {
    map1[char.charCodeAt(0) - "a".charCodeAt(0)] += 1;
  }

  // Initialize map2 with the frequency of characters in the first window of s2
  for (let i = 0; i < s1.length; i++) {
    map2[s2.charCodeAt(i) - "a".charCodeAt(0)] += 1;
  }

  let left = 0; // Start index of the window
  let right = s1.length - 1; // End index of the window

  // Slide the window across s2
  while (right < s2.length) {
    // If the current window matches the frequency count of s1, return true
    if (map2.every((count, index) => count === map1[index])) {
      return true;
    }

    // Remove the character going out of the window from map2
    map2[s2.charCodeAt(left) - "a".charCodeAt(0)] -= 1;
    left += 1; // Move the window to the right

    right += 1; // Expand the window to the right
    if (right < s2.length) {
      // Add the new character coming into the window to map2
      map2[s2.charCodeAt(right) - "a".charCodeAt(0)] += 1;
    }
  }

  // After sliding through s2, check if the last window matches
  return map2.every((count, index) => count === map1[index]);
};
