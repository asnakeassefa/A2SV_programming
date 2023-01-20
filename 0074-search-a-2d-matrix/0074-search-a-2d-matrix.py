class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        row = len(matrix)
        
        for i in range(row):
            if matrix[i][-1] >= target:
                if target in matrix[i]:
                    return True
                else:
                    return False