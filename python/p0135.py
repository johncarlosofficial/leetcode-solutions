from typing import List

class Solution:
    def candy(self, ratings: List[int]) -> int:
        # If there's only one child, just give them 1 candy.
        if len(ratings) == 1:
            return 1
        
        # Initialize a list `candy` where each child gets at least one candy.
        # We start by giving 1 candy to every child.
        candy = [1] * len(ratings)
        
        # First pass: Traverse from left to right to ensure children with higher ratings than
        # the previous child get more candies than their left neighbor.
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                # If the current child's rating is higher than the previous child,
                # give the current child one more candy than the previous child.
                candy[i] = candy[i-1] + 1
        
        # Second pass: Traverse from right to left to ensure children with higher ratings than
        # the next child get more candies than their right neighbor.
        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i+1]:
                # If the current child's rating is higher than the next child,
                # make sure they have more candies than the next child.
                # Only update if the current child doesn't already have enough candies.
                if candy[i] <= candy[i+1]:
                    candy[i] = candy[i+1] + 1
        
        # The total number of candies needed is the sum of the `candy` list.
        return sum(candy)
