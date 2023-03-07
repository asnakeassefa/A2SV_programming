class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1 :
            return 0
        mid = 2 ** (n-1) // 2
        if k > mid:
            if self.kthGrammar(n-1, (k-1) % mid+1) == 0:
                return 1
            elif self.kthGrammar(n-1 , (k-1) % mid+1) == 1:
                return 0
        else:
            return self.kthGrammar(n-1,k)