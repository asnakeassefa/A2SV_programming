class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ptr1 = 0
        ptr2 = 1
        length = len(nums)
        while ptr2 < length:
            if nums[ptr1] >= nums[ptr2]:
                ptr2 += 1
                continue
            ptr1 += 1
            nums[ptr1] = nums[ptr2]
            ptr2 += 1
        return ptr1+1