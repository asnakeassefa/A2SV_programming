class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        array = defaultdict(set)
        # ans = True
        row = len(matrix)
        col = len(matrix[0])
        
        for i in range(row):
            for j in range(col):
                array[i-j].add(matrix[i][j])
                if len(array[i-j]) > 1:
                    return False
        
        return True