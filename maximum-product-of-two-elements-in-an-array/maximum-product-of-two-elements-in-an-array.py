class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxx = 0
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                prod = (nums[i] - 1) * (nums[j] - 1)
                if prod>maxx:
                    maxx = prod
        return maxx             
        