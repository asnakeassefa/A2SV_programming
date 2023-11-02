class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        @cache
        def dp(idx,isBuying,numT):
            if idx >= len(prices):
                return 0
            if numT == 2:
                return 0
            
            if isBuying:
                ans = max(dp(idx+1,False,numT)-prices[idx],dp(idx+1,True,numT))
            else:
                ans = max(dp(idx+1,True,numT+1)+prices[idx],dp(idx+1,False,numT))

            return ans

        return dp(0,True,0)
            