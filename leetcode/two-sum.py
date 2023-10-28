class Solution(object):
    def twoSum(self, nums, target):
        dic = {}

        for i,num in enumerate(nums):
            diff = target - num
            if diff in dic:
                return [i,dic[diff]]
            dic[num] = i