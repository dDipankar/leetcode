import heapq  as hq
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        min_heap = []
        rows = len(matrix)
        cols = len(matrix[0])
        x = min(k, rows)
        
        for i in range(0,x):
            min_heap.append((matrix[i][0],i,0))
        hq.heapify(min_heap)
        while k:
            num,row,col = hq.heappop(min_heap)
            if col<cols-1:
                hq.heappush(min_heap,(matrix[row][col+1],row,col+1))
            k -= 1
        return num