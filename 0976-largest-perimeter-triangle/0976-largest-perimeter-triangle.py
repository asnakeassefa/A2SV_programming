class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        ans = 0
        length = len(nums)
        
        nums.sort()
        for i in range(length-2):
            s = nums[i] + nums[i+1] + nums[i+2]
            temp = s/2
            if ((temp-nums[i])*(temp-nums[i+1])*(temp-nums[i+2])) > 0:
                ans = max(ans,s)
            else:
                continue
        return ans