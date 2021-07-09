"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution(object):
    def height(self,treenode):
        if not treenode:
            return 0
        if len(treenode.children)==0:
            return 0
        max_h1 = 0
        max_h2 = 0
        for child in treenode.children:
            h = self.height(child)+1 
            if h >max_h1:
                temp = max_h1
                max_h1 = h
                max_h2 = temp
            elif h> max_h2:
                max_h2 = h
        height = max_h1+ max_h2
        self.diam = max(self.diam, height)
        
        return max_h1
    def diameter(self, root):
        """
        :type root: 'Node'
        :rtype: int
        """
        self.diam = 0
        
        
        d = self.height(root)
        
        return self.diam