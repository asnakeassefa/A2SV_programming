class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        length = len(nums)
        nums.sort()
        left = 0
        right = length - 1
        ans = 0
        while left < right:
            if nums[right] + nums[left] > k:
                right -= 1
            elif nums[right] + nums[left] < k:
                left += 1
            elif nums[right] + nums[left] == k:
                ans += 1
                left += 1
                right -= 1
        
        return ans