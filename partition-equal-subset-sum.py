class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        if total % 2:
            return False
        def dp(nums,idx,total,runSum,memo):
            if idx == len(nums):
                return False
            if (idx,runSum) in memo:
                return memo[(idx,runSum)]
            if runSum == total//2:
                memo[(idx,runSum)] = True
                return True
            
            memo[(idx,runSum)] = dp(nums,idx+1,total,runSum+nums[idx],memo) or dp(nums,idx+1,total,runSum,memo)

            return memo[(idx,runSum)]
        return dp(nums,0,total,0,{})