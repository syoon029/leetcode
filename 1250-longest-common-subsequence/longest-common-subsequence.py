class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """

        m = len(text1)
        n = len(text2)
        
        c = [[0 for i in range(n+1)] for j in range(m+1)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                if (text1[i-1] == text2[j-1]):
                    c[i][j] = c[i-1][j-1] + 1
                else:
                    c[i][j] = max(c[i-1][j], c[i][j-1])
        
        return c[m][n]
        