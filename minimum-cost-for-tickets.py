class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        memo = {}
        def dp(idx,days,costs):
            if idx >= len(days):
                return 0
            if idx in memo:
                return memo[idx]

            ans = float('inf')
            for i in range(3):
                validDays = days[idx] + [0,6,29][i]
                low = bisect.bisect_right(days,validDays)
                ans = min(ans,dp(low,days,costs) + costs[i])
            memo[idx] = ans
            return memo[idx]

        return dp(0,days,costs)