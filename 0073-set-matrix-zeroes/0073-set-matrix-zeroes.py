class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        col = len(matrix[0])
        #used to store index of zeros
        setRow = set()
        setCol = set()
        
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    setRow.add(i)
                    setCol.add(j)
                    
        for i in range(row):
            for j in range(col):
                if i in setRow or j in setCol:
                    matrix[i][j] = 0