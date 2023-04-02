class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        length = len(nums)
        for i in range(length):
            if nums[i] == i+1:
                continue
            while nums[i] != i+1:
                to = nums[i]
                if nums[to-1] == to:
                    return nums[to-1]
                temp = nums[to-1]
                nums[to-1] = nums[i]
                nums[i] = temp