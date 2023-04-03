class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        last = n & 1
        n >>= 1
        while n:
            if (n&1) != last:
                last = n & 1
                n >>= 1
            else:
                return False
        return True