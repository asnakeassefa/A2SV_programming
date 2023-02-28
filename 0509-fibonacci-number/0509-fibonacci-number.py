class Solution:
    def memo(self,n,Dict):
        if n == 1: return 1
        if n == 0: return 0
        
        if Dict.get(n):
            return Dict[n]
        
        ans = self.memo(n-1,Dict) + self.memo(n-2,Dict)
        Dict[n] = ans
        return ans
    def fib(self, n: int) -> int:
        Dict = dict()
        return self.memo(n,Dict)