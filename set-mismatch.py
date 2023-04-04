class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        dup=None
        miss=None
        length = len(nums)
        for i in range(length):
            while i+1 != nums[i]:
                if nums[i] == nums[nums[i]-1]:
                    dup = nums[i]
                    break
                temp = nums[nums[i]-1]
                nums[nums[i]-1] = nums[i]
                nums[i] = temp
        for i,num in enumerate(nums):
            if i+1 != num:
                miss = i+1
        return [dup,miss]