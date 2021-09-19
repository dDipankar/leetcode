from collections import Counter
class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        tt = Counter()
        for ch in t:
            tt[ch]+=1
        for ch in s:
            tt[ch] -=1
        
        for key in tt:
            if tt[key]>0:
                return key
                
        
        
        