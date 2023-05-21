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
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        length = len(s)
        UF = UnionFind(length)
        for pair in pairs:
            UF.union(pair[0],pair[1])
        store = defaultdict(list)
        for i,char in enumerate(s):
            heapq.heappush(store[UF.find(i)],char)
        ans = ""
        for i in range(length):
            ans += heapq.heappop(store[UF.find(i)])

        return ans