class Solution(object):
    def dfs(self, grid, row, col):
        nr = len(grid)
        nc = len(grid[0])
        if row<0 or col<0 or row>=nr or col>=nc or grid[row][col]=='0':
            return
        
        grid[row][col] = '0'
        self.dfs(grid,row-1,col)
        self.dfs(grid,row, col-1)
        self.dfs(grid,row+1,col)
        self.dfs(grid,row,col+1)
        
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        numIslands = 0
        nr = len(grid)
        nc = len(grid[0])
        
        for r in range(0,nr):
            for c in range(0,nc):
                if grid[r][c]=='1':
                    numIslands +=1
                    self.dfs(grid,r,c)
        return numIslands 