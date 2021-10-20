class Solution(object):
    def __init__(self):
        self.paths = []
    def dfs(self, node,graph,path):
        if node == len(graph)-1:
            self.paths.append(list(path))
            return
        nodes = graph[node]
        for n in nodes:
            path.append(n)
            self.dfs(n,graph,path)
            path.pop()
            
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        path = []
        path.append(0)
        self.dfs(0,graph,path)
        return self.paths
        
        