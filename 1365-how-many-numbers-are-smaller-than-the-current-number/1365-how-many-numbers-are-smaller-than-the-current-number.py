class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        counter = defaultdict(int)
        newNums = sorted(nums)
        for i,num in enumerate(newNums):
            if num not in counter:
                counter[num] = i
        
        return [counter[num] for num in nums]