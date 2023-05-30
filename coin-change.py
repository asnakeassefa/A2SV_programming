class Solution:
    def dp(self,coins,amount,memo):
        if amount in memo:
            return memo[amount]
        
        MinCount = float('inf')
        for coin in coins:
            if amount-coin >= 0:
                value = self.dp(coins,amount-coin,memo)
                MinCount = min(value+1,MinCount)
        memo[amount] = MinCount
        return MinCount
    def coinChange(self, coins: List[int], amount: int) -> int:
        val = self.dp(coins,amount,{0:0})
        if val == float('inf'):
            return -1
        return val