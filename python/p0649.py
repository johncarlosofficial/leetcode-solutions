from collections import deque


class Solution:

    def predictPartyVictory(self, senate: str) -> str:
        queue_r = deque()
        queue_d = deque()

        for i in range(len(senate)):
            if senate[i] == "R":
                queue_r.append(i)
            else:
                queue_d.append(i)

        while queue_r and queue_d:
            r = queue_r.popleft()
            d = queue_d.popleft()

            if r < d:
                queue_r.append(r + len(senate))
            else:
                queue_d.append(d + len(senate))

        return "Radiant" if queue_r else "Dire"
