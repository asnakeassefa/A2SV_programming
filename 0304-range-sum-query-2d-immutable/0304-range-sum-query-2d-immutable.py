class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        col = len(matrix[0])
        row = len(matrix)
        self.presum = []
        tempSum = [0] * (col+1)
        self.presum.append(tempSum)
        
        for i in range(row):
            tempSum = [0]
            tempSum.extend(list(accumulate(matrix[i])))
            self.presum.append(tempSum)
        # print(self.presum)
        for j in range(col+1):
            for i in range(1,row+1):
                self.presum[i][j] += self.presum[i-1][j]
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # print(self.presum)
        ans = self.presum[row2+1][col2+1]-self.presum[row2+1][col1] - self.presum[row1][col2+1] + self.presum[row1][col1]
        return ans
# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)