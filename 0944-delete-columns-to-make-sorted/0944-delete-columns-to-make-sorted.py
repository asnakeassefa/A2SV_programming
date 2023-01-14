class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        ans = 0
        for j in range(len(strs[0])):
            tempVal = []
            for i in range(len(strs)):
                tempVal.append(ord(strs[i][j]))
            temp = tempVal.copy()
            temp.sort()
            if tempVal != temp:
                ans += 1
                
        return ans