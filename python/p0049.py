from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Using defaultdict(list) means if we try to access a key that doesn't exist, 
        # it will automatically create an empty list for that key.
        anagrams = defaultdict(list)
        
        for word in strs:
            # Create an array of 26 zeros. Each index corresponds to a letter in the alphabet.
            # For example, index 0 is for 'a', index 1 is for 'b', ..., index 25 is for 'z'.
            count = [0] * 26
            
            # Count the frequency of each character in the word.
            for char in word:
                # ord(char) - ord('a') gives the index for the character.
                # For example, ord('a') - ord('a') is 0, ord('b') - ord('a') is 1, ..., ord('z') - ord('a') is 25.
                count[ord(char) - ord('a')] += 1
            
            # Convert the count array to a tuple, so it can be used as a key in the dictionary.
            key = tuple(count)
            
            # Append the word to the list of words that have the same character frequency.
            anagrams[key].append(word)
        
        # Return the values of the dictionary, which are lists of anagrams.
        return list(anagrams.values())