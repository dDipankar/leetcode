class Solution(object):
    def getpvt(self, nums):
        low = 0
        high = len(nums) -1  
        while(high >= low):
            mid = (low+high)//2
            #print(mid)
            if nums[mid]>nums[mid+1]:
                return mid+1
            if nums[mid]<nums[mid-1]:
                return mid
            if nums[mid]>nums[low]:
                low = mid+1
            else:
                high = mid - 1

    def binsearch(self,nums, target):
        low = 0
        high = len(nums) -1
        while(high >= low):
                mid = (low+high)//2
                if nums[mid] == target:
                    return mid
                if target>nums[mid]:
                    low = mid+1
                else:
                    high = mid - 1
        return -1
    
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums)==1:
            return 0 if nums[0]==target else -1
        if nums[0]<nums[-1]:
            return  self.binsearch(nums, target)
        else:
            pvt_index = self.getpvt(nums)
            print(pvt_index)
            if target == nums[pvt_index]:
                return pvt_index
            if target< nums[0]:
                idx = self.binsearch(nums[pvt_index+1:],target)
                if idx >=0:
                    return pvt_index +1+ idx
                else:
                    return -1
            else:
                return self.binsearch(nums[0:pvt_index], target)
