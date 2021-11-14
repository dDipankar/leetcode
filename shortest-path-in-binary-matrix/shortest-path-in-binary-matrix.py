class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m,n = len(grid), len(grid[0])
        
        if grid[0][0] == 1 or grid[m-1][n-1]==1: return -1
        
        q = [(0,0,1)]
        
        grid[0][0]=1
        neignbours = [(0,1), (1,0), (0, -1), (-1, 0), (1,1), (1,-1), (-1,1), (-1,-1)]
        while q:
            for  _ in range(len(q)):
                i,j, path_len= q.pop(0)
                if (i,j) ==(m-1, n-1): return path_len
                for dx,dy in neignbours:
                    x = i+dx
                    y = j +dy
                    if (x>=0) and (y>=0) and (x<m) and (y<n) and (grid[x][y]==0):
                            q.append((x,y,path_len+1))
                            grid[x][y] = 1
                            #print(q)
            
        return -1