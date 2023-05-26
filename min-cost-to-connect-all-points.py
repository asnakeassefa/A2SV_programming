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
        return self.find(x) == self.find(y)
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        length = len(points)
        UF = UnionFind(length)
        ans = 0
        arr = []
        for i in range(length):            
            for j in range(length):
                x = abs(points[i][0]-points[j][0])
                y = abs(points[i][1]-points[j][1])
                val = x + y
                arr.append((val,i,j))

        arr.sort()
        for val,i,j in arr:
            if not UF.connected(i,j):
                UF.union(i,j)
                ans+=val
        return ans