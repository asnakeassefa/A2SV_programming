class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        length = len(nums)
        arr = [1 for i in range(length)]

        for i,num in enumerate(nums):
            idx = i-1
            max_ = 0
            while idx > -1:
                if nums[idx] < nums[i]:
                    max_ = max(max_,arr[idx])
                idx -= 1
            arr[i] += max_
        return max(arr)