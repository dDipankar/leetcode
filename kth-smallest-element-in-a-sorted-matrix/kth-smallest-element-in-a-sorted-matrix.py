import heapq  as hq
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        minheap_queue = []
        
        rows = len(matrix)
        cols = len(matrix[0])
        
        x = min(k,rows)
        
        for i in range(0,x):
            minheap_queue.append((matrix[i][0],i,0))
        hq.heapify(minheap_queue)
        
        while k:
            num, row, col = hq.heappop(minheap_queue)
            if col<cols-1: 
                hq.heappush(minheap_queue,(matrix[row][col+1],row,col+1))
            k-=1
            
        return num