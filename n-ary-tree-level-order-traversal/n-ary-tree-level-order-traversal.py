"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if not root:
            return []
        queue = []
        queue.append(root)
        output = []
        #output.append([])
        #print(queue)
        while(queue):
            level = []
            for _ in range(len(queue)):
                a = queue.pop(0)
                level.append(a.val)
                queue.extend(a.children)
            output.append(level)
        return output