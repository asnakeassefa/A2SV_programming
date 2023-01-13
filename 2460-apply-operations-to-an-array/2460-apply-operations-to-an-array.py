class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        ptr = 0
        ans = []
        countZero = 0
        length = len(nums)
        while ptr < length:
            if ptr < length and nums[ptr] == 0:
                countZero += 1
                ptr += 1
            elif ptr + 1 < length and nums[ptr] == nums[ptr + 1]:
                ans.append(nums[ptr] * 2)
                ptr += 2
                countZero += 1
            else:
                ans.append(nums[ptr])
                ptr += 1
                
        for _ in range(countZero):
            ans.append(0)
        
        return ans