class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        ptr1 = 0
        ptr2 = k
        Sum = 0
        ans = -float('inf')
        length = len(nums)
        for i in range(k):
            Sum += nums[i]
        ans = max(ans,Sum)
        while ptr2 < length:
            Sum -= nums[ptr1]
            Sum += nums[ptr2]
            ptr1 += 1
            ptr2 += 1
            ans = max(ans,Sum)
        return ans/k