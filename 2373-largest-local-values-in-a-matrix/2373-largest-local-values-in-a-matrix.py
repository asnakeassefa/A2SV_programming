class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        ans = []
        row = len(grid)
        col = len(grid[0])
        
        for i in range(row - 2):
            rowMax = []
            for j in range(col - 2):
                temp = []
                temp.append(max(grid[i][j:j+3]))
                temp.append(max(grid[i+1][j:j+3]))
                temp.append(max(grid[i+2][j:j+3]))
                rowMax.append(max(temp))
            ans.append(rowMax)
        return ans