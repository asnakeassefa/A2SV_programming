class Solution:
    def dp(self,idx,nums,memo):
        if idx == len(nums)-1:
            return nums[idx]
        
        if idx >= len(nums):
            return 0
        
        if idx in memo:
            return memo[idx]
        
        memo[idx] = max(self.dp(idx+1,nums,memo), (self.dp(idx+2,nums,memo)+nums[idx]))
        return memo[idx]
    def rob(self, nums: List[int]) -> int:
        length = len(nums)
        if length == 1:
            return nums[0]
        ans = max(self.dp(0,nums[1:],{}),self.dp(0,nums[:length-1],{}))
        return ans