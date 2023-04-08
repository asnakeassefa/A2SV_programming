class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        length = len(nums)
        ans = []
        for index in range(length):
            while index != nums[index]-1:
                if nums[nums[index]-1] == nums[index]:
                    break
                temp = nums[nums[index]-1]
                nums[nums[index]-1] = nums[index]
                nums[index] = temp
        for i,num in enumerate(nums):
            if i + 1 != num:
                ans.append(i+1)
        return ans