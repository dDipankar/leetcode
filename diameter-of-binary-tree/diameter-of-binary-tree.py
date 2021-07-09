# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# see video: https://www.youtube.com/watch?v=ey7DYc9OANo
class Solution(object):
    def height(self, treenode ):
        if treenode == None:
            return 0
        left = self.height(treenode.left)
        right = self.height(treenode.right)
        if left > right:
            h = 1 + left
        else:
            h = 1 + right
        self.diam = max(self.diam, left+right)    
        return h
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.diam =0
        hh = self.height(root)
        
        return self.diam
        
