class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        rotate = {0:(0,1),1:(1,0),2:(0,-1),3:(-1,0)}
        val = {"R":1,"L":-1,"G":0}
        idx = 0
        curr = [0,0]
        for i in range(4):
            for char in instructions:
                if char == "G":
                    curr[0] += rotate[idx][0]
                    curr[1] += rotate[idx][1]
                idx = (idx + val[char]) % 4
        if curr == [0,0]:
            return True
        return False