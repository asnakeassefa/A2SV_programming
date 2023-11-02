class Solution:
    def soupServings(self, n: int) -> float:
        memo = defaultdict(float)
        def dp(a,b):
            if a <= 0 and b<=0:
                return 0.5
            if a <=0 and b > 0:
                return 1
            if b <=0 and a > 0:
                return 0

            if (a,b) in memo:
                return memo[(a,b)]
            
            val1 = dp(a-100,b)
            val1 += dp(a-75,b-25)
            val1 += dp(a-50,b-50)
            val1 += dp(a-25,b-75)
            memo[(a,b)] = 0.25 * val1
            return memo[(a,b)]
        if n >= 4800:
            return 1
        return dp(n,n)