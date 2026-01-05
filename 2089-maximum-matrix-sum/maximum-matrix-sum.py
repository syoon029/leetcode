class Solution(object):
    def maxMatrixSum(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        
        total = 0
        min_abs = float("inf")
        neg = 0
        
        for row in matrix:
            for val in row:
                total += abs(val)
                if val < 0:
                    neg +=1
                min_abs = min(min_abs, abs(val))
        
        if neg % 2 != 0:
            total -= 2 * min_abs
        
        return total