import heapq  # Importing the heapq library to work with a heap (priority queue)

class Solution:
    def longestDiverseString(self, count_a: int, count_b: int, count_c: int) -> str:
        # Initialize an empty result string
        result = ""

        # Initialize a max heap to store characters by frequency (using negative frequency for max heap)
        max_heap = []
        
        # Create a list of character frequencies as tuples of (-frequency, character)
        # Using negative because Python's heapq is a min-heap, so we need to negate to simulate a max-heap
        char_frequencies = [(-count_a, "a"), (-count_b, "b"), (-count_c, "c")]

        # Push only the characters with non-zero frequency into the max heap
        for freq, char in char_frequencies:
            if freq != 0:  # Ignore characters with zero occurrences
                heapq.heappush(max_heap, (freq, char))  # Add (frequency, character) to the heap

        # While there are still characters in the heap
        while max_heap:
            # Pop the character with the highest frequency (most negative frequency)
            freq, char = heapq.heappop(max_heap)

            # Check if the last two characters in the result are the same as the current one
            if len(result) > 1 and result[-1] == result[-2] == char:
                # If we can't add the current character, check if there is another character available
                if not max_heap:
                    break  # No other characters to add, so break the loop
                else:
                    # Pop the second most frequent character and append it to the result
                    freq2, char2 = heapq.heappop(max_heap)
                    result += char2
                    freq2 += 1  # Decrease the frequency since we used one occurrence of char2

                    # If there are still occurrences of char2 left, push it back into the heap
                    if freq2 != 0:
                        heapq.heappush(max_heap, (freq2, char2))

            # If the last two characters are not the same as the current one, append the current character
            else:
                result += char
                freq += 1  # Decrease the frequency since we used one occurrence of char

            # If there are still occurrences of the current character left, push it back into the heap
            if freq != 0:
                heapq.heappush(max_heap, (freq, char))

        # Return the constructed result string
        return result