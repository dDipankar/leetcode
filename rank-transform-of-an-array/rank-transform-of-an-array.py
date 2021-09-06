class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        sorted_arr = sorted(set(arr))
        # make a dictionary where key = array element and value=index+1
        dic = {v:k+1 for k,v in enumerate(sorted_arr)}
        
        # run the dictionary for each array(unsorted) element 
        return [dic[i] for i in arr]
