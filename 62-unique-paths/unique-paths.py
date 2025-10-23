class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m ==1 or n == 1:
            return 1
        
        dp=[[1]* n for _ in range(m)]

        for r in range(1,m):
            for c in range(1,n):
                dp[r][c] = dp[r-1][c] + dp[r][c-1]
        
        return dp[m-1][n-1]

        #return self.uniquePaths(m-1,n) + self.uniquePaths(m,n-1)
        