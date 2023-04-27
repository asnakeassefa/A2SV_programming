class Solution:
    def inbound(self,row,col,grid):
        return 0<= row < len(grid) and 0<= col<len(grid[0])

    def bfs(self,grid):
        count = 1
        directions = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(-1,1),(1,-1),(-1,-1)]
        queue = deque([(0,0)])
        visited = set([(0,0)])
        if grid[0][0]:
            return -1
        if grid[len(grid)-1][len(grid)-1]:
            return -1
        if len(grid) == 1:
            return 1
        while queue:
            length = len(queue)
            count += 1
            for _ in range(length):
                index = queue.popleft()
                for row,col in directions:
                    n_row = index[0] + row
                    n_col = index[1] + col
                    if len(grid)-1 == n_row and len(grid)-1 == n_col:
                        return count
                    if self.inbound(n_row,n_col,grid) and not grid[n_row][n_col] and (n_row,n_col) not in visited:
                        visited.add((n_row,n_col))
                        queue.append((n_row,n_col))
        return -1
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        return self.bfs(grid)