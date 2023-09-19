class Solution:
    def dp(self,curr,n,memo,ans,copied):
        if curr[0] > n:
            return float('inf')
        if curr[0] == n:
            return ans
        if curr in memo:
            return memo[curr]
        if copied:
            memo[curr] = self.dp((curr[0]+curr[1],curr[1]),n,memo,ans+1,False)
        else:
            memo[curr] = min(self.dp((curr[0],curr[0]),n,memo,ans+1,True), self.dp((curr[0]+curr[1],curr[1]),n,memo,ans+1,False))

        return memo[curr]
    def minSteps(self, n: int) -> int:
        if n ==1:
            return 0
        memo = defaultdict(int)
        return self.dp((1,1),n,memo,1,True)