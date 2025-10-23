from collections import deque
class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        max_island = 0 

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    queue = deque([(r,c)])
                    curr = 1
                    grid[r][c] = 0 

                    while queue:
                        cr,cc = queue.popleft()
                        direction = [(0,1),(0,-1),(1,0),(-1,0)]
                        for dr, dc in direction:
                            nr,nc = cr+dr, cc+dc
                            if 0<=nr<len(grid) and 0<=nc<len(grid[0]):
                                if grid[nr][nc] == 1:
                                    queue.append((nr,nc))
                                    grid[nr][nc] = 0
                                    curr += 1

                    max_island = max(max_island, curr)

        return max_island

                
                
        
        # max_island = 0 
        # for r in range(len(grid)):
        #     for c in range(len(grid[0])):

        #         def dfs(i,j):
        #             if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
        #                 return 0 
        #             if grid[i][j] == 0:
        #                 return 0
        #             if grid[i][j] == 1:
        #                 grid[i][j] = 0
        #                 return 1 + dfs(i+1,j) + dfs(i-1,j) + dfs(i, j-1) + dfs(i, j+1)

        #         if grid[r][c] == 1:
        #             max_island = max(max_island, dfs(r,c))
                    

                    

        # return max_island                


                    
