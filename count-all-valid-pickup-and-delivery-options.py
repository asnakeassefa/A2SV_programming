class Solution:
    def countOrders(self, n: int) -> int:
        def dp(val,memo):
            # print(val)
            if val[0] < 0:
                return 0
            if val == (0,0):
                return 1
            if val in memo:
                return memo[val]
            memo[val] = dp((val[0]-1,val[1]),memo) * val[0]
            if val[0] < val[1]:
                memo[val] += dp((val[0],val[1]-1),memo) * (val[1] - val[0])
            # print(memo[val])
            return memo[val]
        return dp((n,n),{}) %( 10 ** 9 + 7)