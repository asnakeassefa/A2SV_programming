class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        nums.sort(reverse = True)
        
        maxsize = max(requests,key = lambda x: x[1])[1]
        
        presum = [0] * (maxsize + 2)
        for request in requests:
            presum[request[0]] += 1
            presum[request[1]+1] -= 1
        
        for i in range(1,maxsize+1):
            presum[i] += presum[i-1]
        
        presum.sort(reverse = True)
        
        ans = 0
        for i in range(maxsize+1):
            ans += presum[i] * nums[i]
        return ans % (10 ** 9 + 7)