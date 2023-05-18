class UnionFind:
    def __init__(self):
        self.rep = {chr(ord('a')+i):chr(ord('a')+i) for i in range(27)}
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
        return self.find[x] == self.find[y]
class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        length = len(s1)
        UF = UnionFind()
        for i in range(length):
            UF.union(s1[i],s2[i])
        ans = ""
        for char in baseStr:
            ans += UF.find(char)
        return ans