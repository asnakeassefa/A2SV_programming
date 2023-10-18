class UnionFind:
    def __init__(self):
        self.rep = {i:i for i in range(26)}
        self.size = {i:1 for i in range(26)}
    def find(self, x):
        parent = self.rep[x]
        while parent != self.rep[parent]:
            parent = self.rep[parent]
        if x < parent:
            self.rep[x] = x
            self.rep[parent] = x
            return x
        while x != parent:
            x_parent = self.rep[x]
            self.rep[x] = parent
            x = x_parent
        
        return parent
		
    def union(self, x, y):
        x_rep = self.find(x)
        y_rep = self.find(y)

        if x_rep == y_rep:
            return
        
        if x_rep > y_rep:
            x_rep , y_rep = y_rep, x_rep

        self.rep[y_rep] = x_rep
    def connected(self, x, y):
        return self.find(x) == self.find(y)
class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        length = len(s1)
        UF = UnionFind()
        for i in range(length):
            UF.union((ord(s1[i])-ord('a')),(ord(s2[i])-ord('a')))
        s = "abcdefghijklmnopqrstuvwxyz"
        ans = ""
        for char in baseStr:
            idx = UF.find(ord(char)-ord('a'))
            ans += s[idx]

        return ans