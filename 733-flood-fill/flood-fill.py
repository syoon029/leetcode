from collections import deque

class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        if image[sr][sc] == color:
            return image
        
        original = image[sr][sc]
        image[sr][sc] = color

        queue = deque([(sr,sc)])
        direction = [(0,1),(0,-1),(1,0),(-1,0)]

        while queue:
            cr,cc = queue.popleft()
            for dr,dc in direction:
                nr,nc = cr+dr, cc+dc
                if 0<=nr < len(image) and 0<=nc<len(image[0]):
                    if image[nr][nc] == original:
                        image[nr][nc] = color
                        queue.append((nr,nc))
        
        return image




        # if image[sr][sc] == color:
        #     return image

        # original= image[sr][sc]

        # def dfs(i,j):
        #     if i < 0 or i >= len(image) or j < 0 or j >= len(image[0]):
        #         return
        #     if image[i][j] != original:
        #         return
        #     image[i][j] = color

        #     dfs(i,j+1)
        #     dfs(i,j-1)
        #     dfs(i+1,j)
        #     dfs(i-1,j)
        
        # dfs(sr,sc)

        # return image

        original_color = image[sr][sc]
    
        if original_color == color:
            return image
        
        queue = deque([(sr,sc)])
        image[sr][sc] = color

        while queue:
            r, c = queue.popleft()
            direction = [(0,1),(0,-1), (1,0), (-1,0)]
            for dr,dc in direction:
                nr, nc = r+dr, c+dc
                if (0 <= nr < len(image) and 0 <= nc < len(image[0]) and image[nr][nc] == original_color):
                    image[nr][nc] = color
                    queue.append([nr,nc])
        
        return image
                
            

            

        
        
        
        
        


       
                

        