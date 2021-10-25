# Followed the approach of Coreman's DFS: Chapter 22
from collections import defaultdict
class Solution(object):
    def build_graph(self, n, edges,adjacency_list):
        for e in edges:
            adjacency_list[e[0]].append(e[1])
        #self.color = ['WHITE'] *n
        return adjacency_list
    
    def dfs(self, n, edges, node, destination, adjacency_list,color):
        print(node)
        if color[node] != None:
            return color[node] == 'BLACK'
        if len(adjacency_list[node])==0:
            return node == destination
        color[node] = 'GREY'
        for neighbour in adjacency_list[node]:
            if not self.dfs(n, edges, neighbour, destination, adjacency_list,color):
                return False
            
        color[node] = 'BLACK'
        return True
    def leadsToDestination(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        adjacency_list = defaultdict()
        for i in range(0,n):
            adjacency_list[i] = []
            
        adjacency_list = self.build_graph(n, edges, adjacency_list)
        color = [None]*n
        count = 0
        '''
        
        for (key, value) in adjacency_list.iteritems():
            if len(value)==0:
                count +=1
        if count>1:
            return False
            
        '''
        return self.dfs(n, edges, source, destination, adjacency_list,color)
        