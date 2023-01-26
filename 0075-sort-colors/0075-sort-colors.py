class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        num1 = 0
        num2 = 0
        num3 = 0
        
        for num in nums:
            if num == 0:
                num1 += 1
            elif num == 1:
                num2 += 1
            elif num == 2:
                num3 += 1
        length = len(nums)
        
        for i in range(num1):
            nums[i] = 0
        for i in range(num2):
            nums[i+num1] = 1
        for i in range(num3):
            nums[i+num1+num2] = 2