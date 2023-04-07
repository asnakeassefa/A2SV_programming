class Solution:
    def minSteps(self, n: int) -> int:
        if n ==1:
            return 0
        d = 2
        ans = 0
        while d * d <= n:
            while n % d == 0:
                n //= d
                ans += d
            d += 1
        if n > 1:
            ans += n
        return ans