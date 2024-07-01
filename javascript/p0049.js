/**
 * @param {string[]}
 * @return {string[][]}
 */
export var groupAnagrams = function (strs) {
  // Initialize an empty object to hold our groups of anagrams.
  let anagrams = [];

  // Iterate through each word in the input array.
  for (let word of strs) {
    // Create an array of 26 zeros. Each index corresponds to a letter in the alphabet.
    // For example, index 0 is for 'a', index 1 is for 'b', ..., index 25 is for 'z'.
    let key = new Array(26).fill(0);

    for (let char of word) {
      // Increment the count at the position corresponding to the character.
      key[char.charCodeAt(0) - "a".charCodeAt(0)] += 1;
    }

    // Convert the count array to a string, so it can be used as a key in the object.
    let keyString = key.toString();

    // If the key already exists in the object, append the word to the list.
    // Otherwise, create a new key with the word in a list.
    if (keyString in anagrams) {
      anagrams[keyString].push(word);
    } else {
      anagrams[keyString] = [word];
    }
  }

  // Return the values of the object, which are arrays of anagrams.
  return Object.values(anagrams);
};
