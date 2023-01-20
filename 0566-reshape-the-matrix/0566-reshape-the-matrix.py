class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        newArray = []
        newCol = 0
        row = len(mat)
        col = len(mat[0])
        temp = []
        if row * col != r * c:
            return mat
        
        for i in range(row):
            for j in range(col):
                if len(temp) == c:
                    newArray.append(temp)
                    temp = []
                temp.append(mat[i][j])
                if len(temp) == c:
                    newArray.append(temp)
                    temp = []
        return newArray       
                    