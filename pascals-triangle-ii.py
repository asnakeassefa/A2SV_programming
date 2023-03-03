class Solution:
    def getVal(self,row,col,memo):
        if row == 0 or row == 1 or col == 0 or col == row:
            return 1
        if (row,col) in memo:
            return memo[(row,col)]
        memo[(row,col)] = self.getVal(row-1,col-1,memo) + self.getVal(row-1,col,memo)
        return memo[(row,col)]
    def getRow(self, rowIndex: int) -> List[int]:
        ans = []
        memo = {}
        for i in range(rowIndex+1):
            ans.append(self.getVal(rowIndex,i,memo))
        return ans