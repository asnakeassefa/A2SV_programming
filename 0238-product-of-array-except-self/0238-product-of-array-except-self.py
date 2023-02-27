class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1]
        post = []
        length = len(nums)
        temp = 1
        for num in nums:
            temp *= num
            pre.append(temp)
        
        temp = 1
        for i in range(length-1,-1,-1):
            temp *= nums[i]
            post.append(temp)
        post.reverse()
        post.append(1)
        ans = []
        print(post)
        for i in range(length):
            ans.append(pre[i] * post[i+1])
        return ans