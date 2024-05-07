from typing import List


class Solution:

    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        return self.recursive(asteroids)

    def recursive(self, asteroids: List[int]) -> List[int]:
        stack = []
        changed = False

        for i in range(len(asteroids)):
            if asteroids[i] > 0:
                stack.append(asteroids[i])
            else:
                if stack:
                    if stack[-1] < 0:
                        stack.append(asteroids[i])
                    elif abs(asteroids[i]) > stack[-1]:
                        changed = True
                        stack[-1] = asteroids[i]
                    elif abs(asteroids[i]) == stack[-1]:
                        changed = True
                        stack.pop()
                else:
                    stack.append(asteroids[i])

        if not changed:
            return stack
        else:
            return self.recursive(stack)
