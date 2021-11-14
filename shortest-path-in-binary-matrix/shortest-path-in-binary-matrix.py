from collections import deque
class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m,n = len(grid), len(grid[0])
    
        if grid[0][0] ==1 or grid[m-1][n-1]==1: return -1
        
        q= [(0,0)]
        path_len =1
        
        while q:
            new_q = []
            
            for i,j in q:
                if (i,j) ==(m-1, n-1): return path_len
                
                grid[i][j]=1
                for x,y in [(i+1,j), (i-1, j), (i-1, j-1), (i+1, j+1), (i,j-1), (i+1,j-1), (i-1,j+1), (i,j+1)]:
                    if x<0 or y<0 or x>=m or y>=n or grid[x][y]==1: continue
                    
                    new_q.append((x,y))
                    grid[x][y] = 1
                    
            q= new_q
            path_len+=1
            
        return -1
        