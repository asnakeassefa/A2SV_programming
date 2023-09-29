class Solution:

    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m = len(dungeon[0])
        n = len(dungeon)
        arr = [[-float('inf') for i in range(m+1)] for i in range(n+1)]

        for i in range(n-1,-1,-1):
            for j in range(m-1,-1,-1):
                if i == n-1 and j == m-1:
                    if dungeon[i][j] <= 0:
                        arr[i][j] = dungeon[i][j] - 1
                    else:
                        arr[i][j] = dungeon[i][j]
                    continue
                val1 = arr[i][j+1]
                val2 = arr[i+1][j]
                val = max(val1,val2)
                
                if val > 0:
                    if dungeon[i][j] <= 0:
                       arr[i][j] = dungeon[i][j] - 1
                    else:
                        arr[i][j] = dungeon[i][j]
                else:
                    if dungeon[i][j] + val == 0:
                        arr[i][j] = -1
                    else:
                        arr[i][j] = dungeon[i][j] + val

        
        if arr[0][0] > 0:
            return 1
        else:
            return -arr[0][0]