class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        right = len(nums) -1
        nn = right
        left = 0
        arr_tmp = [None] * (right+1)
        while right>=left:
            if abs(nums[right]) < abs(nums[left]):
                arr_tmp[nn] = abs(nums[left]) 
                left = left +1
            elif abs(nums[right]) >= abs(nums[left]):
                arr_tmp[nn] = abs(nums[right])
                right = right -1
            nn = nn-1
        return [x*x for x in arr_tmp]