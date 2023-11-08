class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        inc = True
        dec = True
        length = len(nums)
        for i in range(1,length):
            if nums[i] < nums[i-1]:
                inc = False
        for i in range(1,length):
            if nums[i] > nums[i-1]:
                dec = False
        
        return inc or dec