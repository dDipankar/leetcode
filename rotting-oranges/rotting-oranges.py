class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        queue = []
        fresh_fruit = 0
        etime = -1
        nrows = len(grid)
        ncols = len(grid[0])
        neighbors = [(1,0),(-1,0),(0,1),(0,-1)]
        
        for i in range(nrows):
            for j in range(ncols):
                if grid[i][j]==2:
                    queue.append((i,j))
                elif grid[i][j]==1:
                    fresh_fruit +=1
        if fresh_fruit ==0:
            return 0
        while(queue):
            for _ in range(len(queue)):
                r,c = queue.pop(0)
                for dr, dc in neighbors:
                    rr = r +dr
                    cc = c + dc
                    
                    if rr>=0 and cc>=0 and rr<nrows and cc<ncols and grid[rr][cc] == 1:
                        grid[rr][cc] = 2
                        queue.append((rr,cc))
                        fresh_fruit -=1
            etime +=1
            
        return etime if fresh_fruit ==0 else -1
                        
                
                    