class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        memo = defaultdict(int)

        def dp(idx,canBuy):
            if idx >= len(prices):
                return 0
            
            if (idx,canBuy) in memo:
                return memo[(idx,canBuy)]
            ans = 0
            if canBuy:
                ans = max(dp(idx+1,not canBuy)-prices[idx], dp(idx+1,canBuy))
            else:
                ans = max(dp(idx+1,not canBuy)+(prices[idx] - fee),dp(idx+1,canBuy))

            memo[(idx,canBuy)] = ans

            return ans

        return dp(0,True)