class Solution:
    def sqroot(self,num):
        temp = int(math.sqrt(num))
        return temp ** 2 == num
    
    def judgeSquareSum(self, c: int) -> bool:
        length = int(math.sqrt(c) + 1)
        for num in range(length):
            num2 = c-(num ** 2)
            if self.sqroot(num2):
                return True
        return False