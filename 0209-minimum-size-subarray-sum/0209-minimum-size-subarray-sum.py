class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ptr1 = 0
        ptr2 = 0
        length = len(nums)
        Sum = 0
        ans = float('inf')
        
        while ptr2 < length:
            Sum += nums[ptr2]
            while Sum >= target:
                ans = min(ans,ptr2-ptr1+1)
                Sum -= nums[ptr1]
                ptr1 += 1
            ptr2 += 1
        if ans == float('inf'):
            return 0
        return ans