class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def dp(amount, coins, dic):
            if amount in dic:
                return dic[amount]
            
            res = float('inf')
            for coin in coins:
                if amount - coin >= 0:
                    res = min(res, dp(amount - coin, coins, dic))
                
            dic[amount] = res + 1
            return dic[amount]
        
        res = dp(amount, coins, {0:0})
        if res == float('inf'):
            res = -1
        return res