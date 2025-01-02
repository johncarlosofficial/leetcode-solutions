class Solution:
    def uniquePaths(self, rows: int, cols: int) -> int:
        # Dictionary to store computed factorials for memoization
        factorial_cache = {}

        # Calculate the total number of moves required to reach the bottom-right corner.
        # This includes (rows - 1) down moves and (cols - 1) right moves.
        total_moves = rows + cols - 2

        # Number of down moves needed.
        down_moves = rows - 1

        # Number of right moves needed.
        right_moves = cols - 1

        # Define a helper function to compute the factorial of a number.
        # Uses memoization to store previously computed values.
        def factorial(num):
            # Base cases: 0! = 1 and 1! = 1
            if num == 1 or num == 0:
                return 1

            # If the factorial has already been computed, return the cached value.
            if num in factorial_cache:
                return factorial_cache[num]
            else:
                # Compute the factorial recursively and store it in the cache.
                result = num * factorial(num - 1)
                factorial_cache[num] = result
                return result

        # Compute the numerator of the combination formula, which is (total_moves)!.
        numerator = factorial(total_moves)

        # Compute the denominator of the combination formula, which is (down_moves)! * (right_moves)!.
        denominator = factorial(down_moves) * factorial(right_moves)

        # The number of unique paths is the result of the combination formula:
        # C(total_moves, down_moves) = numerator / denominator
        # Return the integer value of the division.
        return numerator // denominator  # Integer division ensures we avoid floating-point results.

        # Time Complexity:
        # 1. The factorial function is called for total_moves, down_moves, and right_moves.
        #    Each factorial computation has a time complexity of O(n), where n is the input to the function.
        # 2. With memoization, redundant calculations are avoided, and each factorial is computed only once.
        # 3. Therefore, the overall time complexity is O(rows + cols), as total_moves = rows + cols - 2.

        # Space Complexity:
        # 1. Recursive stack depth for factorial computation is O(max(rows, cols)).
        # 2. Memoization dictionary stores at most total_moves, down_moves, and right_moves factorials.
        # 3. Total space complexity: O(rows + cols).