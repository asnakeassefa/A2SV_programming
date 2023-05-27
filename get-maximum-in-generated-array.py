class Solution:
    def solve(self,idx,memo):
        if idx <= 0:
            return 0
        if idx == 1:
            return 1
        if idx == 2:
            return 1
        
        if memo.get(idx):
            return memo[idx]
        if idx % 2 == 0:
            memo[idx] = self.solve(idx//2,memo)
            return memo[idx]
        if idx % 2 != 0:
            memo[idx] = self.solve(idx//2,memo) + self.solve(idx//2 + 1,memo)
            return memo[idx]

    def getMaximumGenerated(self, n: int) -> int:
        memo = {}
        ans = 0
        for i in range(n+1):
            ans = max(ans,self.solve(i,memo))
            
        return ans