class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1]
        post = []
        length = len(nums)
        temp = 1
        #build pre mul
        for num in nums:
            temp *= num
            pre.append(temp)
        #build post mul
        temp = 1
        for i in range(length-1,-1,-1):
            temp *= nums[i]
            post.append(temp)
        post.reverse()
        post.append(1)
        ans = []
        for i in range(length):
            ans.append(pre[i] * post[i+1])
        return ans