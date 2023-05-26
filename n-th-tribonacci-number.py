class Solution:
    def solve(self,n,memo):
        if n < 1:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1
        
        if memo.get(n):
            return memo[n]

        memo[n] = self.solve(n-1,memo) + self.solve(n-2,memo) + self.solve(n-3,memo)
        return memo[n]
    def tribonacci(self, n: int) -> int:
        return self.solve(n,{})