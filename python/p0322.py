from typing import List, Optional

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        min_coins_needed = [amount + 1] * (amount + 1)
        min_coins_needed[0] = 0
        
        for current_amount in range(1, amount + 1):
            for coin in coins:
                if current_amount - coin >= 0:
                    min_coins_needed[current_amount] = min(min_coins_needed[current_amount], min_coins_needed[current_amount - coin] + 1)
                    
        return min_coins_needed[-1] if min_coins_needed[-1] != amount + 1 else -1
    