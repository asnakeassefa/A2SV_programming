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
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        Uf = UnionFind(n)
        for edge in edges:
            Uf.union(edge[0],edge[1])
        
        return Uf.find(source) == Uf.find(destination)