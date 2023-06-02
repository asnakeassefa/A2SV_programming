class Solution:
    def dp(self,nums,target,idx,temp,memo):
        if idx == len(nums) and temp == target:
            return 1
        if idx >= len(nums):
            return 0
        if (idx,temp) in memo:
            
            return memo[(idx,temp)]
        
        value1 = self.dp(nums,target,idx+1,temp+nums[idx],memo)
        value2 = self.dp(nums,target,idx+1,temp-nums[idx],memo)
        memo[(idx,temp)] = value1 + value2
        return memo[(idx,temp)]
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        return self.dp(nums,target,0,0,{})