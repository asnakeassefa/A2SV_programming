class Solution:
    def search(self, nums: List[int], target: int) -> int:
        length =  len(nums)

        low = 0
        high = length-1

        while low < high:
            mid = low + (high-low)//2
            if mid+1 < length and nums[0] < nums[mid] and nums[mid] < nums[mid+1]:
                low = mid + 1
            else:
                high = mid
            if mid+1 < length and nums[0] < nums[mid] and nums[mid] > nums[mid+1]:
                low = mid
                break

        pivot = low
        low = 0
        high = pivot

        while low < high:
            mid = low + (high-low)//2
            if target > nums[mid]:
                low = mid + 1
            else:
                high = mid
        if nums[low] == target:
            return low
        
        low = pivot+1
        high = length-1

        while low < high:
            mid = low + (high-low)//2
            if target > nums[mid]:
                low = mid + 1
            else:
                high = mid
        if low < length and nums[low] == target:
            return low

        return -1
