# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def get_depth(self, node: TreeNode) -> int:
        d = 0
        while node.left:
            node = node.left
            d =d+1
        return d
    def exists(self, idx:int, depth:int, node:TreeNode) -> bool:
        left, right = 0, 2**depth - 1
        for _ in range(0,depth):
            mid = left + (right - left)//2
            if idx<= mid:
                right = mid
                node = node.left
            else:
                left = mid+1
                node = node.right
        return  node is not None    
    
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        #count = 0
        #if root == None:
            #return count
        #N1 = self.countNodes(root.left)
        #N2 = self.countNodes(root.right)
        #count = 1 + N1 + N2
        #return count
        
        if root == None:
            return 0
        dep = self.get_depth(root)
        
        if dep == 0:
            return 1
        
        
        left, right = 0, 2**dep-1
        
        while left<=right:
            mid = left + (right - left) // 2
            if self.exists(mid,dep,root):
                left = mid+1
            else:
                right = mid - 1
                
        return (2**dep-1) + left