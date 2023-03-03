class Solution:
    def invert(self,val):
        ans = ""
        for char in val:
            if char == "0":
                ans += "1"
            elif char == "1":
                ans += "0"
        return ans
    def buildBits(self,n):
        if n == 0:
            return "0"
        ans = self.buildBits(n-1)
        ans += "1" + self.invert(ans)[::-1]
        return ans
    def findKthBit(self, n: int, k: int) -> str:
        final = self.buildBits(n-1)
        return final[k-1]