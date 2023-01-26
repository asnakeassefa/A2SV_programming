class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        length = len(nums)
        count = [0]*length;
        for x in range(length):
            for y in range(length):
                if(nums[x] > nums[y]):
                    count[x] += 1
        return count