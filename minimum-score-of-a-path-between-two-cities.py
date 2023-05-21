class UnionFind:
    def __init__(self, n):
        self.rep = {i:i for i in range(n+1)}
        self.size = {i:1 for i in range(n+1)}
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
        return self.find[x] == self.find[y]
class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        roadCost = defaultdict(lambda:float("inf"))
        UF = UnionFind(n)
        for road in roads:
            root1 = UF.find(road[0])
            min1 = roadCost[UF.find(root1)]
            root2 = UF.find(road[1])
            min2 = roadCost[UF.find(root2)]
            UF.union(root1,root2)
            roadCost[UF.find(root1)] = min(min1,min2,road[2])
        ans = roadCost[UF.find(1)]
        return ans