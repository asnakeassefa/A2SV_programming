class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = set()
        length = len(nums)
        j = 0
        for i in range(length):
            while i+1 != nums[i]:
                if nums[i] == nums[nums[i]-1]:
                    ans.add(nums[i])
                    break
                temp = nums[(nums[i]-1)]
                nums[(nums[i]-1)] = nums[i]
                nums[i] = temp
        return ans