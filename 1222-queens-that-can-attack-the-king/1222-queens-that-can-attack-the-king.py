class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        ans = []
        # travling vertically
        up = king[0]
        while up >= 0:
            if [up,king[1]] in queens:
                ans.append([up,king[1]])
                break
            up -= 1
        # travling down vetically
        down = king[0] + 1
        while down < 8:
            if [down,king[1]] in queens:
                ans.append([down,king[1]])
                break
            down += 1
        # travling left horizontally
        left = king[1] - 1
        while left >= 0:
            if [king[0],left] in queens:
                ans.append([king[0],left])
                break
            left -= 1
        #travling right horizontally
        right = king[1] + 1
        while right < 8:
            if [king[0],right] in queens:
                ans.append([king[0],right])
                break
            right += 1
        # travling diagonl up left
        for i in range(1,king[0] + 1):
            if [king[0]-i,king[1]-i] in queens:
                ans.append([king[0]-i,king[1]-i])
                break
        # travling digonal down right
        for i in range(1,9-king[1]):
            if [king[0]+i,king[1]+i] in queens:
                ans.append([king[0]+i,king[1]+i])
                break
        # travling digonal up right
        for i in range(1,9-king[1]):
            if [king[0]-i,king[1]+i] in queens:
                ans.append([king[0]-i,king[1]+i])
                break
        #travling digonal down left
        for i in range(1,9-king[0]):
            if [king[0]+i,king[1]-i] in queens:
                ans.append([king[0]+i,king[1]-i])
                break
        
        return ans