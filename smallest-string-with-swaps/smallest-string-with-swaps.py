from collections import defaultdict
class Solution(object):
    def smallestStringWithSwaps(self, s, pairs):
        """
        :type s: str
        :type pairs: List[List[int]]
        :rtype: str
        """
        n = len(s)
        uf = UnionFind(n)
        for p in pairs:
            uf.union(p[0],p[1])
        dict_c = defaultdict(list)
        dict_i = defaultdict(list)
        
        for i in range(0, n):
            dict_i[uf.find(i)].append(i) 
            dict_c[uf.find(i)].append(s[i])
        
        result = [None]*len(s)
        for key in dict_c:
            dict_c[key].sort()
            indices = list(dict_i[key])
            chrs = list(dict_c[key])
            for i in range(len(indices)):
                result[indices[i]] =chrs[i]
                
        return "".join(result)
            
            
# UnionFind class
class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1] * size
        
    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    # The union function with union by rank
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1

    def connected(self, x, y):
        return self.find(x) == self.find(y)