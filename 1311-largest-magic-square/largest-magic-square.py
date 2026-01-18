class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        res = 1

        def isvalid(i,j,k):
            su = None
            for x in range(i,i+k):
                row = sum(grid[x][j:j+k])
                if su is None:
                    su = row
                elif su!= row:
                    return False
            
                    
            for y in range(j, j + k):
                current_col_sum = 0
                for x in range(i, i + k):
                    current_col_sum += grid[x][y]
                
                if current_col_sum != su:
                    return False

        
            if sum(grid[i+d][j+d] for d in range(k)) != su:
                return False
            
            if sum(grid[i + d][j + k - 1 - d] for d in range(k)) != su:
                return False
            
            return True


        for k in range(2, min(m, n) + 1):
            for i in range(m - k + 1):
                for j in range(n - k + 1):
                    if isvalid(i, j, k):
                        res = k
        return res
                

        