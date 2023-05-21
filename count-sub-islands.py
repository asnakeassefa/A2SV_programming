class Solution:
    def inbound(self,idx,grid):
        return 0<=idx[0]<len(grid) and 0<=idx[1]<len(grid[0])
    
    def dfs(self,grid1,grid,visited,curr,flag):
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        if curr in visited and not self.inbound(curr,grid):
            return
        visited.add(curr)
        if grid1[curr[0]][curr[1]] == 0:
            flag[0] = False
        for row,col in directions:
            x = curr[0] + row
            y = curr[1] + col
            if (x,y) not in visited and self.inbound((x,y),grid) and grid[x][y] == 1:
                if grid1[x][y] == 0:
                    flag[0] = False
                self.dfs(grid1,grid,visited,(x,y),flag)
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        visited = set()
        ans = 0
        for i,row in enumerate(grid2):
            for j,col in enumerate(row):
                flag = [True]
                if col == 1 and (i,j) not in visited:
                    self.dfs(grid1,grid2,visited,(i,j),flag)
                    if flag[0]:
                        ans += 1
        return ans