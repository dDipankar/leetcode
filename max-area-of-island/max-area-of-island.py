class Solution(object):
    def dfs(self, grid, row, col):
        nr = len(grid)
        nc = len(grid[0])
        count = 1
        if row<0 or col<0 or row>=nr or col>=nc or grid[row][col]==0:
            return 0
        
        
        grid[row][col] = 0
        count += self.dfs(grid,row-1,col)
        count += self.dfs(grid,row, col-1)
        count += self.dfs(grid,row+1,col)
        count += self.dfs(grid,row,col+1)
        
        return count
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        area = 0
        nr = len(grid)
        nc = len(grid[0])
        
        for r in range(0,nr):
            for c in range(0,nc):
                if grid[r][c]==1:
                    area = max(area,self.dfs(grid,r,c))
        return area