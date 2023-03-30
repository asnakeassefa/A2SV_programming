class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        i = 1
        while i < 32:
            ans += n & 1
            ans = ans << 1
            n = n >> 1
            i += 1
        if n:
            ans += n & 1
        return ans