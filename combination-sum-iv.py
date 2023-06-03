class Solution:
    def dp(self,nums,num,value,target,memo):
        if value == target:
            return 1
        if value > target:
            return 0
        temp = 0
        if value in memo:
            return memo[value]
        for i,num in enumerate(nums):
            temp += self.dp(nums,num,value+num,target,memo)
        memo[value] = temp
        return temp
    def combinationSum4(self, nums: List[int], target: int) -> int:
        return self.dp(nums,0,0,target,{})