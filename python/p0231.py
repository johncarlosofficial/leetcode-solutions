class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # Check if n is less than 1. If so, it can't be a power of two.
        if n < 1:
            return False
        
        # If n is exactly 1, return True because 1 is 2^0, which is a power of two.
        if n == 1:
            return True
        
        # Otherwise, check if n is even (divisible by 2).
        else:
            if n % 2 == 0:
                # If n is even, divide it by 2 and call the function recursively.
                return self.isPowerOfTwo(n / 2)
            else:
                # If n is odd and greater than 1, it can't be a power of two.
                return False

# Create an instance of the Solution class.
solution = Solution()

# Test the isPowerOfTwo method with the value 8 and print the result.
# Since 8 is 2^3, the function should return True.
print(solution.isPowerOfTwo(8))

class Solution2:
    def isPowerOfTwo(self, n: int) -> bool:
        # A number n is a power of two if and only if it is greater than 0
        # and has exactly one bit set in its binary representation.
        return n > 0 and (n & (n - 1)) == 0

# Create an instance of the Solution2 class.
solution2 = Solution2()

# Test the isPowerOfTwo method with the value 8 and print the result.
# Since 8 is 2^3, the function should return True.
print(solution2.isPowerOfTwo(8))
