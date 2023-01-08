class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        rowSum = []
        colSum = defaultdict(int)
        n = len(grid)
        m = len(grid[0])
        ans = []
        #build column sum and row sum
        for i in range(n):
            for j in range(m):
                colSum[j] += grid[i][j]
            rowSum.append(sum(grid[i]))
        #bulding the result
        columnSum = []
        for colval in colSum.values():
            columnSum.append(colval)
        
        for i in range(n):
            temp = []
            for j in range(m):
                val = rowSum[i] + columnSum[j] - (m - columnSum[j]) - (n - rowSum[i])
                temp.append(val)
            print(temp)
            ans.append(temp)
        return ans
        