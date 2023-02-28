class Solution:
    def recu(self,n,Dict):
        if n == 1: return 1
        if n == 0: return 0
        
        if Dict.get(n):
            return Dict[n]
        
        ans = self.recu(n-1,Dict) + self.recu(n-2,Dict)
        Dict[n] = ans
        return ans
    def fib(self, n: int) -> int:
        Dict = dict()
        return self.recu(n,Dict)