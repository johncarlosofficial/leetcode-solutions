class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        drank = numBottles
        
        while numBottles >= numExchange:
            drank += numBottles // numExchange
            numBottles = numBottles // numExchange + numBottles % numExchange
            
        return drank