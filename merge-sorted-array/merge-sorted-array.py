class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        
        if n==0:
            print('m')
            return nums1
        if m==0:
            nums1[:] = nums2[:]
            return nums1
        else:
            nums1_copy = nums1[:m]
            left = 0
            right = 0
            i = 0
            while i<(m+n):
                # right>=n will be used for simple copy when right array is completed
                if (right>=n) or (left < m and nums1_copy[left]<=nums2[right]):
                    nums1[i] = nums1_copy[left]
                    left = left+1
                else:
                    nums1[i] = nums2[right]
                    right = right+1
                i = i+1
            return nums1