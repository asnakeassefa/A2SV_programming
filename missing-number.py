class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        length = len(nums) + 1
        for i in range(length):
            if i not in nums:
                return i