class Solution:
    def inbound(self,idx,grid):
        return 0<= idx[0] < len(grid) and 0<= idx[1] < len(grid[0])
    def dfs(self,grid,curr,visited):
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        if curr in visited:
            return
        visited.add(curr)
        for row,col in directions:
            x = row + curr[0]
            y = col + curr[1]
            if (x,y) not in visited and self.inbound((x,y),grid) and grid[x][y] == 'O':
                self.dfs(grid,(x,y),visited)
        
    def solve(self, board: List[List[str]]) -> None:
        visited = set()
        row = len(board)
        col = len(board[0])

        for i in range(col):
            if board[0][i] == 'O' and (0,i) not in visited:
                self.dfs(board,(0,i),visited)
        for i in range(row):
            if board[i][0] == 'O' and (i,0) not in visited:
                self.dfs(board,(i,0),visited)
        for i in range(col):
            if board[row-1][i] == 'O' and (row-1,i) not in visited:
                self.dfs(board,(row-1,i),visited)
        for i in range(row):
            if board[i][col-1] == 'O' and (i,col-1) not in visited:
                self.dfs(board,(i,col-1),visited)
        for i in range(row):
            for j in range(col):
                if (i,j) not in visited:
                    board[i][j] = 'X'