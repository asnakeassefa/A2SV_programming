class Solution:
    def maxSubarrays(self, nums: List[int]) -> int:
        temp = int("11111111111111111111111111111111",2)
        ones = temp
        
        length = len(nums)
        for i in range(length):
            ones &= nums[i]
        count = 0
        if ones > 0:
            count = 1
        else:
            ones = temp
            for i in range(length):
                ones &= nums[i]
                if ones == 0:
                    count += 1
                    if i < length-1:
                        ones = temp

        return count