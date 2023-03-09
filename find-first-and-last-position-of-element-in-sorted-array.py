class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] < target:
                low = mid + 1
            elif nums[mid] >= target:
                high = mid - 1
        final = low

        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] <= target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
        
        if final >= len(nums) or nums[final] != target:
            return [-1,-1]
        return [final,low - 1]