class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        res = 0
        for index,num in enumerate(nums):
            for val in nums[index+1:]:
                if num == val:
                    res += 1
        return res