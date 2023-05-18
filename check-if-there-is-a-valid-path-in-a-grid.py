class UnionFind:
    def __init__(self, n,m):
        self.rep = {(i,j):(i,j) for i in range(n) for j in range(m)}
        self.size = {(i,j):1 for i in range(n) for j in range(m)}
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
    def inbound(self,idx,grid):
        return 0<=idx[0]<len(grid) and 0<=idx[1]<len(grid[0])
    
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        n = len(grid)
        m = len(grid[0])
        neighbors = {
                  1: [(0, -1, {1, 4, 6}), (0, 1, {1, 3, 5})],
                  2: [(1, 0, {2, 5, 6}), (-1, 0, {2, 3, 4})],
                  3: [(0, -1, {1, 4, 6}), (1, 0, {2, 5, 6})],
                  4: [(1, 0, {2, 5, 6}), (0, 1, {1, 3, 4})],
                  5: [(-1, 0, {2, 3, 4}), (0, -1, {1, 4, 6})],
                  6: [(-1, 0, {2, 3, 4}), (0, 1, {1, 3, 5})]
              }
        UF = UnionFind(n,m)
        stack = [(0,0)]
        visited = set((0,0))
        while stack:
            print(stack)
            idx = stack.pop()
            for i,j,streets in neighbors[grid[idx[0]][idx[1]]]:
                x = idx[0] + i
                y = idx[1] + j
                if (x,y) not in visited and self.inbound((x,y),grid) and grid[x][y] in streets:
                    stack.append((x,y))
                    visited.add((x,y))
                    UF.union(idx,(x,y))

        return UF.connected((0,0),(n-1,m-1))