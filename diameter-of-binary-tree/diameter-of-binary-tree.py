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
        return h
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        lh = self.height(root.left)
        #print(lh)
        rh = self.height(root.right)
        #print(rh)
        ld = self.diameterOfBinaryTree(root.left)
        rd = self.diameterOfBinaryTree(root.right)
        print(ld)
        d = max(lh+rh, max(ld,rd))
        
        return d
        
