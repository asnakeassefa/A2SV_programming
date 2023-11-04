class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        Min = float(inf)
        Max = -1
        for i,val in enumerate(prices):
            if val < Min:
                Max = 0
                Min = val
            if val > Max:
                Max = val
                ans = max(ans,(Max-Min))

        return ans