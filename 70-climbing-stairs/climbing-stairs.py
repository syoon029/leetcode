class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return n

        dp = [0] * n # 0+1번째를 올라갈 때 사용가능한 방법
        dp[0] = 1 # only 1
        dp[1] = 2 # 1+1 or 2

    
        for i in range(2,n):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[n-1]


