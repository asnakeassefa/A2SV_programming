class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        ans = 0
        while max(x,y):
            num1 = x & 1
            num2 = y & 1
            ans += num1 ^ num2
            x = x >> 1
            y = y >> 1
        return ans