class UnionFind:
    def __init__(self, size):
        self.rep = {i:i for i in range(size)}
        self.size = {i:1 for i in range(size)}
    def find(self, x):
        if self.rep[x] == x:
            return x
        y = self.find(self.rep[x])
        self.rep[x] = y
        return y
    def union(self, x, y):
        xrep = self.find(x)
        yrep = self.find(y)
        
        if self.size[xrep] > self.size[yrep]:
            self.rep[yrep] = xrep
            self.size[xrep] += self.size[yrep]
        else:
            self.rep[xrep] = yrep
            self.size[yrep] += self.size[xrep]
    def connected(self, x, y):
        return self.find(x) == self.find(y)
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        length = len(edges)
        UF = UnionFind(length+1)
        ans = []
        for edge in edges:
            if UF.connected(edge[0],edge[1]):
                ans = edge
            UF.union(edge[0],edge[1])
        return ans