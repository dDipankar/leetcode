"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    # visited[old node] = new clone node
    visited = {}
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if node == None:
            return None
        new_node = Node(node.val,[])
        self.visited[node] = new_node
        
        for nei in node.neighbors:
            if nei not in self.visited:
                self.cloneGraph(nei)
                
            # if the neibouring node is already cloned then find the clone node    
            node = self.visited[nei] 
            new_node.neighbors.append(node)
            
        return new_node