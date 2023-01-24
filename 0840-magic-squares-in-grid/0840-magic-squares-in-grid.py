class Solution:
    def checkGrid(self, subGrid):
        num = sum(subGrid[0])
        # check distinctness
        for i in range(3):
            if len(set(subGrid[i])) != len(subGrid[i]):
                return False
        
        for row in range(3):
            #check sum of row
            if sum(subGrid[row]) != num:
                return False
            # check sum of columen
            colSum = 0
            for col in range(3):
                if subGrid[col][row] > 9 or subGrid[col][row] < 1:
                    return False
                colSum += subGrid[col][row]
            if colSum != num:
                return False
            # check sum of diagonals
            gridUp = 0
            gridDown = 0
            
            for index in range(3):
                gridDown += subGrid[index][index]
                gridUp += subGrid[index][2-index]
            if gridDown != num and gridUp != num:
                return False
        # else
        return True
            
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        
        rowLen = len(grid)-2
        colLen = len(grid[0]) -2
        matrix = []
        count = 0
        for row in range(rowLen):
            for col in range(colLen):
                matrix.append(grid[row][col:col + 3])
                matrix.append(grid[row+1][col: col+3])
                matrix.append(grid[row+2][col: col+3])
                if self.checkGrid(matrix):
                    count += 1
                matrix = []
        return count