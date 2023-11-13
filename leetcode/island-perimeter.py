class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        def inbound(x,y):
            return 0<= x < len(grid) and 0<= y < len(grid[0])
        
        n = len(grid)
        m = len(grid[0])
        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    if not inbound(i-1,j) or grid[i-1][j] == 0:
                        ans +=1
                    if not inbound(i,j-1) or grid[i][j-1] == 0:
                        ans += 1
                    if not inbound(i+1,j) or grid[i+1][j] == 0:
                        ans += 1
                    if not inbound(i,j+1) or grid[i][j+1] == 0:
                        ans += 1
        return ans