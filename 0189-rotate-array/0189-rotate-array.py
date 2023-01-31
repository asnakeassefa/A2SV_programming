class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        right = k % length
        left = length - right
        
        for i in range(right//2):
            nums[left + i],nums[(length-1)-i] = nums[(length-1)-i],nums[left + i]
        print(nums)
        for i in range(left//2):
            nums[i],nums[(left-1)-i] = nums[(left-1)-i],nums[i]
        print(nums)
        for i in range((length//2)):
            nums[i],nums[(length-1)-i] = nums[(length-1)-i],nums[i]
        print(nums)