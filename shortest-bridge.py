class Solution:
    def inbound(self,row,col,grid):
        return 0<=row<len(grid) and 0<=col<len(grid[0])
    def dfs(self,grid,curr,visited,queue):
        direction = [(0,1),(1,0),(-1,0),(0,-1)]
        if curr in visited:
            return
        visited.add(curr)
        queue.append(curr)
        for row,col in direction:
            x = row + curr[0]
            y = col + curr[1]
            if (x,y) not in visited and self.inbound(x,y,grid) and grid[x][y] == 1:
                self.dfs(grid,(x,y),visited,queue)

    def bfs(self,grid,queue,visited):
        direction = [(0,1),(1,0),(-1,0),(0,-1)]
        count = 0
        while queue:
            length = len(queue)
            for _ in range(length):
                node = queue.popleft()
                for row,col in direction:
                    x = node[0] + row
                    y = node[1] + col
                    if (x,y) not in visited and self.inbound(x,y,grid) and grid[x][y] == 1:
                        return count
                    if (x,y) not in visited and self.inbound(x,y,grid):
                        queue.append((x,y))
                        visited.add((x,y))
            count += 1
        
    def shortestBridge(self, grid: List[List[int]]) -> int:
        queue = deque()
        visited = set()
        flag = False
        for i,row in enumerate(grid):
            for j,col in enumerate(row):
                if col == 1:
                    self.dfs(grid,(i,j),visited,queue)
                    flag = True
                    break
            if flag:
                break
        return self.bfs(grid,queue,visited)