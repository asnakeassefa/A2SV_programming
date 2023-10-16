class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == -1:
            return 1/x
        if n == 1:
            return x
        if n == 0:
            return 1
        if n % 2 == 1:
            ans = self.myPow(x,n//2)
            ans *= ans
            return ans * x
        else:
            ans = self.myPow(x,n//2)
            return ans * ans