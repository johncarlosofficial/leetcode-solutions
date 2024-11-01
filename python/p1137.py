class Solution:
    def tribonacci(self, n: int) -> int:
        memoization = {}
        def recursive(n):
            if n == 0:
                return 0
            elif n == 1 or n == 2:
                return 1
            elif n in memoization:
                return memoization[n]
            else:
                result = recursive(n-3) + recursive(n-2) + recursive(n-1)
                memoization[n] = result

                return result

        return recursive(n)
            
        