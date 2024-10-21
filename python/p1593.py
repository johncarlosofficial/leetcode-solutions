class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        # Recursive function to explore splitting the string
        def backtrack(start: int, unique_substrings: set):
            # Base case: If we reached the end of the string, return the number of unique substrings
            if start == len(s):
                return len(unique_substrings)
            
            max_splits = 0 # To store the maximum number of unique splits found
            
            # Try to split the string at every possible position from 'start' to the end
            for end in range(start + 1, len(s) + 1):
                # Get the substring from start to end (end is exclusive)
                substring = s[start:end]

                # If the substring is unique (not already in the set)
                if substring not in unique_substrings:
                    # Add the substring to the set
                    unique_substrings.add(substring)
                    # Recursively call to split the rest of the string from 'end' onwards
                    max_splits = max(max_splits, backtrack(end, unique_substrings))
                    # Remove the substring (backtrack) to try other splits
                    unique_substrings.remove(substring)

            return max_splits # Return the maximum splits found
        
        # Start the backtracking process with an empty set of unique substrings
        return backtrack(0, set())