/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var characterReplacement = function (s, k) {
  // Counts occurrences of characters in the current window
  let dictionary = {};

  // Sliding window pointers
  let left = 0;
  let right = 0;

  // Longest substring found
  let longest = 0;

  while (right < s.length) {
    // Increment count of s[right]
    if (s[right] in dictionary) {
      dictionary[s[right]]++;
    } else {
      dictionary[s[right]] = 1;
    }

    // Shrink window if replacements needed exceed k
    while (right - left + 1 - Math.max(...Object.values(dictionary)) > k) {
      dictionary[s[left]]--;
      if (dictionary[s[left]] === 0) {
        delete dictionary[s[left]];
      }
      left++;
    }

    // Update longest substring length
    longest = Math.max(longest, right - left + 1);
    right++;
  }

  return longest;
};

// Test case
console.log(characterReplacement("AABABBA", 1));
