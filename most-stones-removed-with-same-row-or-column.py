class UnionFind:
    def __init__(self,store):
        self.rep = store
    def find(self, x):
        if self.rep[x] == x:
            return x
        y = self.find(self.rep[x])
        self.rep[x] = y
        return y
    def union(self, x, y):
        xrep = self.find(x)
        yrep = self.find(y)
        
        if self.rep[xrep] < self.rep[yrep]:
            self.rep[yrep] = xrep
        else:
            self.rep[xrep] = yrep
        
    def connected(self, x, y):
        return self.find(x) == self.find(y)

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        length = len(stones)
        size1 = max(stones)
        size2 = max(stones,key = lambda x: x[1])
        
        store = defaultdict(tuple)
        ans = set()

        for i,j in stones:
            store[(i,j)] = (i,j)
        corr = UnionFind(store)
        
        for i in range(length):
            for j in range(length):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    corr.union(tuple(stones[i]),tuple(stones[j]))
        for stone in stones:
            ans.add(corr.find(tuple(stone)))
        return length - len(ans)