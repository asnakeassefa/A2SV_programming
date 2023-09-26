class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        arr = [[0 for j in range(100)] for i in range(100)]
        if poured == 0:
            return 0
        arr[0][0] = poured

        for row in range(99):
            for col in range(row+1):
                leftOver = arr[row][col] - 1
                if leftOver > 0:
                    arr[row][col] = 1
                    arr[row+1][col] += leftOver/2
                    arr[row+1][col+1] += leftOver/2

        return arr[query_row][query_glass]