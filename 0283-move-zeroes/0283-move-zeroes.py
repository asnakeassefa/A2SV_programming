class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = 0
        index = [] * nums.count(0)
        for x in range(len(nums)):
            if nums[x] == 0:
                index.append(x)
        print(index)
        for x in range(len(index)):
            nums.append(nums.pop(index[x] - n))
            n += 1
        