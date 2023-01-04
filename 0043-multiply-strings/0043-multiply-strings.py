class Solution:
	def convertToInt(self,number):
		count = 1
		final = 0
		nums = number[::-1]
		for num in nums:
			final += (ord(num) - ord('0')) * count
			count *= 10
		return final
    
	def multiply(self, num1: str, num2: str) -> str:
		ans = self.convertToInt(num1) * self.convertToInt(num2)
		return str(ans)