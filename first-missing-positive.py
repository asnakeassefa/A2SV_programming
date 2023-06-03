class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        length = len(nums)
        for i in range(length):
            if nums[i] > length or nums[i] <= 0 or nums[i] == i+1:
                continue
            while nums[i] != i+1 and not(nums[i] > length or nums[i] <= 0):
                temp = nums[nums[i]-1]
                if temp == nums[i]:
                    break
                nums[nums[i]-1] = nums[i]
                nums[i] = temp
        
        for i,num in enumerate(nums):
            if i+1 != num:
                return i+1
        return length+1