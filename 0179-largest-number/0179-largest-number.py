class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        length = len(nums)
        
        for i in range(length):
            for j in range(length-1-i):
                if str(nums[j]) + str(nums[j+1]) < str(nums[j+1]) + str(nums[j]):
                    nums[j], nums[j+1] = nums[j+1],nums[j]
        ans = ""
        
        for i in range(length):
            ans += str(nums[i])
            
        if ans[0] == "0":
            return "0"
        return ans