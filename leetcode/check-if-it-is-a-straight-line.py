class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        length = len(coordinates)
        coordinates.sort()
        xflag = True
        yflag = True
        for i in range(1,length):
            if coordinates[i-1][0] != coordinates[i][0]:
                xflag = False
            if coordinates[i-1][1] != coordinates[i][1]:
                yflag = False

        if xflag or yflag:
            return True
        x = abs(coordinates[1][0] - coordinates[0][0])
        y = abs(coordinates[1][1] - coordinates[0][1])
        if y == 0:
            return False
        m = x / y
        for i in range(1,length):
            if  abs(coordinates[i-1][0] - coordinates[i][0]) / abs(coordinates[i-1][1] - coordinates[i][1]) != m:
                return False

        return True