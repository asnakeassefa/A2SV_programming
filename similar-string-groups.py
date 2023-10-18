class UnionFind:
    def __init__(self, size):
        self.rep = [i for i in range(size)]
        self.size = [1 for i in range(size)]
    def find(self, x):
        parent = self.rep[x]
        while parent != self.rep[parent]:
            parent = self.rep[parent]
        
        while x != parent:
            x_parent = self.rep[x]
            self.rep[x] = parent
            x = x_parent
            
        return parent
		
    def union(self, x, y):
        x_rep = self.find(x)
        y_rep = self.find(y)
        
        if self.size[x_rep] > self.size[y_rep]:
            self.rep[y_rep] = x_rep
            self.size[x_rep] += self.size[y_rep]
        else:
            self.rep[x_rep] = y_rep
            self.size[y_rep] += self.size[x_rep]

    def connected(self, x, y):
        return self.find(x) == self.find(y)

class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        length = len(strs)
        UF = UnionFind(length)
        for i in range(length-1):
            for j in range(i+1,length):
                wordlen = len(strs[i])
                count = 0
                for k in range(wordlen):
                    if strs[i][k] != strs[j][k]:
                        count += 1
                if count < 3:
                    UF.union(i,j)

        ans = set()
        for i in range(length):
            ans.add(UF.find(i))
        return len(ans)