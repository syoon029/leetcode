from collections import deque
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        island = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    island += 1
                    grid[i][j] = '0'
                    queue = deque([(i,j)])

                    while queue:
                        r,c = queue.popleft()
                        direction = [(0,1),(0,-1),(1,0),(-1,0)]
                        for dr, dc in direction:
                            nr,nc = r+dr, c+dc
                            if 0<= nr < len(grid) and 0<= nc < len(grid[0]):
                                if grid[nr][nc] == '1':
                                    grid[nr][nc] = '0'
                                    queue.append((nr,nc))

        return island
                

                    
        

        
        # visited = set()
        # island = 0

        # for r in range(len(grid)):
        #     for c in range(len(grid[0])):
        #         if grid[r][c] == '1' and (r,c) not in visited:
        #             island += 1
        #             queue = deque([(r,c)])
        #             visited.add((r,c))
        #             while queue:
        #                 cr,cc = queue.popleft()
        #                 direction = [(0,1),(0,-1),(1,0),(-1,0)]
        #                 for dr,dc in direction:
        #                     nr,nc = cr+dr, cc+dc
        #                     if 0<= nr < len(grid) and 0<= nc < len(grid[0]):
        #                         if grid[nr][nc] == '1' and (nr,nc) not in visited:
        #                             visited.add((nr,nc))
        #                             queue.append((nr,nc))
        
        # return island

        # island = 0
        
        # for r in range(len(grid)):
        #     for c in range(len(grid[0])):
        #         if grid[r][c] == '1':
        #             island += 1
        #             grid[r][c] = '0'
        #             queue = deque([(r,c)])
                
        #             while queue:
        #                 cr,cc = queue.popleft()
        #                 direction = [(0,1),(0,-1), (1,0), (-1,0)]
        #                 for dr, dc in direction:
        #                     nr , nc = cr+dr, cc+dc
        #                     if 0<= nr < len(grid) and 0<= nc < len(grid[0]):
        #                         if grid[nr][nc] == '1':
        #                             grid[nr][nc] = '0'
        #                             queue.append((nr,nc))
            
        # return island
                    
                
                    
                


                

        

        
        
        