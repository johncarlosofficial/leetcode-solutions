class Solution:

    def removeStars(self, s: str) -> str:
        stack = []
        stars = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == '*':
                stars += 1
            else:
                if stars:
                    i += 1
                    stars -= 1
                else:
                    stack.append(s[i])

        # reverse
        left = 0
        right = len(stack) - 1

        while left < right:
            stack[left], stack[right] = stack[right], stack[left]
            left += 1
            right -= 1

        return "".join(stack)
