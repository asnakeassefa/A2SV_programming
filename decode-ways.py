class Solution:
    def dp(self,s,curr,memo):
        if curr<len(s) and s[curr] == "0":
            memo[curr] = 0
            return 0
        if curr >= len(s) - 1:
            return 1

        if curr in memo:
            return memo[curr]
        ans = 0
        if int(s[curr:curr+2]) < 27:
            ans = self.dp(s,curr+2,memo) + self.dp(s,curr+1,memo)
        else:
            ans = self.dp(s,curr+1,memo)

        memo[curr] = ans
        return ans
        
    def numDecodings(self, s: str) -> int:
        
        memo = defaultdict(int)
        return self.dp(s,0,memo)