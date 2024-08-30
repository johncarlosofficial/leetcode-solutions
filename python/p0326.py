class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # Check if n is less than 1. If so, it can't be a power of three.
        if n < 1:
            return False
        
        # If n is exactly 1, return True because 1 is 3^0, which is a power of three.
        if n == 1:
            return True
        
        # Otherwise, check if n is divisible by 3.
        else:
            if n % 3 == 0:
                # If it is, divide it by 3 and call the function recursively.
                return self.isPowerOfTwo(n / 3)
            else:
                # If it is not, it can't be a power of three.
                return False

class Solution2:
    def isPowerOfThree(self, n: int) -> bool:
        # 1162261467 is 3^19, the largest power of 3 that fits in a 32-bit integer
        return n > 0 and 1162261467 % n == 0