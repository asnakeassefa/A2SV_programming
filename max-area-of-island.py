class Solution:
    def travers(self,grid,ans,visited):
        row = len(grid)
        col = len(grid[0])
        temp = [0]
        for i in range(row):
            for j in range(col):
                if grid[i][j] and (i,j) not in visited:
                    self.DFS(grid,i,j,visited,temp)
                    ans[0] = max(ans[0],temp[0])
                    temp = [0]
    def inbound(self,grid,row,col):
        return 0<=row<len(grid) and 0<=col<len(grid[0])
    def DFS(self,grid,row,col,visited,temp):
        direction = [(0,1),(0,-1),(1,0),(-1,0)]

        if not self.inbound(grid,row,col) or not grid[row][col]:
            return
        temp[0] += 1
        visited.add((row,col))
        for a_row,a_col in direction:
            new_row = row + a_row
            new_col = col + a_col
            if (new_row,new_col) not in visited:
                self.DFS(grid,new_row,new_col,visited,temp)
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans = [0]
        self.travers(grid,ans,set())
        return ans[0]