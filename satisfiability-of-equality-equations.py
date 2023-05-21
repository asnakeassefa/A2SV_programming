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
        return self.find(x) == self.find(y)
class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        words = UnionFind()
        set1 = set()
        set2 = set()
        for word in equations:
            if word[1] == "=":
                words.union(word[0],word[3])
        for word in equations:
            if word[1] == "!":
                if words.find(word[0]) == words.find(word[3]):
                    return False
        return True