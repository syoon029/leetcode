class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        #dp
        result = 1
        seq = 1
        
        for i in range(1, len(prices)):
            if prices[i-1] -1 == prices[i] :
                seq += 1
            else:
                seq = 1

            result += seq
        
        return result
