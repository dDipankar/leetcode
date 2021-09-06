class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        high = len(nums)-1
        low = 0
        if len(nums)==1:
            return nums[0]
        # already sorted. Just return the first elemet 
        if nums[low]< nums[high]:
            return nums[low]
        else:
            while high >= low:
                mid = (low+high) //2
                if (nums[mid]< nums[mid-1]):
                    return nums[mid]
                if nums[mid]>nums[mid+1]:
                    return nums[mid+1]
                if nums[0]<nums[mid]:
                    low = mid+1
                else:
                    high = mid-1

        