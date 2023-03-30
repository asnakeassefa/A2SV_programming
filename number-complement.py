class Solution:
    def findComplement(self, num: int) -> int:
        ans = 0
        temp = 0
        while num:
            new = 0
            new += not (num & 1)
            new <<= temp
            ans |= new
            temp += 1
            num >>= 1
        return ans