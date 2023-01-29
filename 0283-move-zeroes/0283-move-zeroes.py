class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        holder = 0
        runner = 0
        while runner < length:
            while holder < length and nums[holder] != 0:
                holder += 1
            while runner < length and nums[runner] == 0:
                runner += 1
            if runner < length and holder < length and holder < runner:
                nums[holder],nums[runner] = nums[runner],nums[holder]
                holder += 1
            runner += 1