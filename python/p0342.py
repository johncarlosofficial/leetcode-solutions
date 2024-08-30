class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # Check if n is less than 1. If so, it can't be a power of four.
        if n < 1:
            return False
        
        # If n is exactly 1, return True because 1 is 4^0, which is a power of four.
        if n == 1:
            return True
        
        # Otherwise, check if n is divisible by four.
        else:
            if n % 4 == 0:
                # If n divisible by four, divide it by 4 and call the function recursively.
                return self.isPowerOfFour(n / 4)
            else:
                # Otherwise, it can't be a power of four.
                return False


solution = Solution()
print(solution.isPowerOfFour(8))

class Solution2:
    def isPowerOfFour(self, n: int) -> bool:
        # Check if n is positive and a power of two
        # (n > 0): Ensure the number is positive
        # (n & (n - 1)) == 0: Check if n is a power of two
        # (n - 1) % 3 == 0: Check if the power of two is a power of four
        return n > 0 and (n & (n - 1)) == 0 and (n - 1) % 3 == 0

# Create an instance of the Solution2 class.
solution2 = Solution2()
print(solution2.isPowerOfFour(8))
