class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        zeroPtr = 0
        ptr = 0
        length = len(nums)
        while ptr < length:
            while ptr < length and nums[ptr] == 0:
                ptr += 1
            while zeroPtr < length and nums[zeroPtr] != 0:
                zeroPtr += 1
            if ptr >= length or zeroPtr >= length:
                break
            if zeroPtr > ptr:
                ptr = zeroPtr + 1
                continue
            nums[zeroPtr],nums[ptr] = nums[ptr],nums[zeroPtr]
            ptr += 1
            zeroPtr += 1