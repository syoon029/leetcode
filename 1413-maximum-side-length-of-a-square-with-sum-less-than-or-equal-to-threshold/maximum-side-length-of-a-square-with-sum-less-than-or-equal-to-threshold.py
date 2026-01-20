class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m = len(mat)
        n = len(mat[0])
        cumulated_sum = [[0]*(n+1) for i in range(m+1)]
        for x in range(1,m+1):
            for y in range(1,n+1):
                cumulated_sum[x][y] = cumulated_sum[x-1][y] + cumulated_sum[x][y-1] + mat[x-1][y-1] - cumulated_sum[x-1][y-1]

        min_len = 0
        k=1
        ans = 0
        for x in range(1, m+1):
            for y in range(1,n+1):
                while k <= min(x,y):
                    cur_sum = cumulated_sum[x][y] - cumulated_sum[x-k][y] - cumulated_sum[x][y-k] + cumulated_sum[x-k][y-k]
                    if cur_sum <= threshold:
                        ans = k
                        k += 1 
                    else:
                        break

        return ans


      