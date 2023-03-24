class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        arr = []
        def backtrack(idx):
            if len(arr) > 1:
                ans.add(tuple(arr))
            if idx == len(nums):
                return
            if not arr or arr[-1] <= nums[idx]:
                arr.append(nums[idx])
                backtrack(idx+1)
                arr.pop()
            backtrack(idx+1)
        backtrack(0)
        return ans