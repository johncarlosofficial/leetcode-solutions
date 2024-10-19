class Solution:
    def findKthBit(self, n: int, k: int) -> str:

        def helper(n: int):
            if n == 1:
                return "0"

            prev = helper(n-1)
            inv = invert(prev)
            rev = reverse(inv)

            return prev + "1" + rev

        
        def invert(binary_string: str) -> str:
            binary_string = list(binary_string)

            for i in range(len(binary_string)):
                if binary_string[i] == "0":
                    binary_string[i] = "1"
                else:
                    binary_string[i] = "0"

            return "".join(binary_string)
            


        def reverse(binary_string: str) -> str:
            binary_string = list(binary_string)

            left = 0
            right = len(binary_string) - 1

            while left < right:
                binary_string[left], binary_string[right] = binary_string[right], binary_string[left]
                left += 1
                right -= 1

            return "".join(binary_string)


        ans = helper(n)

        return ans[k-1]