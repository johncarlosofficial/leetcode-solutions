class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # List to hold the position and speed pairs
        ps = []
        for i in range(len(position)):
            ps.append([position[i], speed[i]])

        # Sort the list based on the car positions in ascending order
        ps.sort(key=lambda x : x[0])

        # Stack to keep track of car fleets
        stack = []
        for i in range(len(ps) -1, -1, -1):
            if not stack:
                stack.append(ps[i])
            else:
                time1 = (target - stack[-1][0]) / stack[-1][1]
                time2 = (target - ps[i][0]) / ps[i][1]

                # If the current car takes longer to reach the target, it forms a new fleet
                if time1 < time2:
                    stack.append(ps[i])

        # The number of car fleets is the size of the stack
        return len(stack)
