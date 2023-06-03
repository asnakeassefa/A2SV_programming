class Solution:
    def backtrack(self,nums,arr,ans):
        if len(arr) == len(nums):
            ans.append(arr)
            return
        for num in nums:
            if num in arr:
                continue
            self.backtrack(nums,arr + [num],ans)

    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        self.backtrack(nums,[],ans)
        return ans