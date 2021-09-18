class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        low = 1
        high = len(nums) - 1
        
        while(low<=high):
            mid = (low+high)//2
            count = sum(num<=mid for num in nums)
            
            if count>mid:
                high = mid-1
                duplicate = mid
            else:
                low = mid+1
        
        return duplicate
        