class Solution:
    def inbound(self,m,n,curr):
        return 0<=curr[0]<m and 0<=curr[1]<n
    
    def dp(self,m,n,curr,memo):
        if curr in memo:
            return memo[curr]
        
        changes = [(1,0),(0,1)]
        total = 0
        for change in changes:
            x = curr[0] + change[0]
            y = curr[1] + change[1]
            if self.inbound(m,n,(x,y)):
                total += self.dp(m,n,(x,y),memo)
        memo[curr] = total
        return total
    def uniquePaths(self, m: int, n: int) -> int:
        return self.dp(m,n,(0,0),{(m-1,n-1):1})