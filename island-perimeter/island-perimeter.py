class Solution(object):
    def dfs(self, grid, row,col):
        nr = len(grid)
        nc = len(grid[0])
        
        if row<0 or col<0 or row>=nr or col>=nc or grid[row][col] ==0:
            return 1
        if grid[row][col] == -1:
            return 0
        
        
        grid[row][col] =-1
        
        count = 0 
        count += self.dfs(grid, row-1, col)
        count += self.dfs(grid, row+1, col)
        count += self.dfs(grid, row, col-1) 
        count += self.dfs(grid, row, col+1)
        return count
                          
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        nr = len(grid)
        nc = len(grid[0])
        p =0
        for row in range(0, nr):
            for col in range(0,nc):
                if grid[row][col]==1:
                    p = self.dfs(grid,row,col)
        return p