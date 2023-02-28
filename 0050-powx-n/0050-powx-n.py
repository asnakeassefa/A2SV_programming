class Solution:
    
    def myPow(self, x: float, n: int) -> float:
        
        if n == 0:
            return 1
        if n == 1:
            return x
        if n > 0:
            if n % 2 != 0:
                ans = self.myPow(x,(n-1)//2)
                return x * ans * ans
            else:
                ans = self.myPow(x,n//2)
                return ans * ans
        if n < 0:
            if n % 2 != 0:
                ans = self.myPow(1/x,-(n-1)//2)
                return x * ans * ans
            else:
                ans = self.myPow(1/x,-n//2)
                return ans * ans
        