class compair(str):
    def __lt__(x,y):
        return x+y > y+x

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        length = len(nums)
        nums[:] = map(str,nums)
        
        # for i in range(length):
        #     for j in range(length-1-i):
        #         if str(nums[j]) + str(nums[j+1]) < str(nums[j+1]) + str(nums[j]):
        #             nums[j], nums[j+1] = nums[j+1],nums[j]
        nums.sort(key=compair)
        ans = ""
        
        for i in range(length):
            ans += str(nums[i])
            
        if ans[0] == "0":
            return "0"
        return ans