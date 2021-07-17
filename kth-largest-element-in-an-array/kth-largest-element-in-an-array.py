import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        q = heapq.nlargest(k,nums)[-1]
        
        return q
    
# runtime O(n log k)

# see https://docs.python.org/3/library/heapq.html
        
        