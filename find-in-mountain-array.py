# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        low = 0
        length = mountain_arr.length() - 1
        high = length
        p = 0

        while low < high:
            mid = low + (high-low)//2
            if mountain_arr.get(mid) < mountain_arr.get(mid+1):
                low = mid + 1
            else:
                high = mid
        p = low

        low = 0
        high = p
        while low < high:
            mid = low + (high-low)//2
            if mountain_arr.get(mid) < target:
                low = mid + 1
            else:
                high = mid
        if mountain_arr.get(low) == target:
            return low        
        low = p
        high = length
        while low < high:
            mid = low + (high-low)//2
            val = mountain_arr.get(mid)
            if val > target:
                low = mid + 1
            else:
                high = mid
        if mountain_arr.get(low) == target:
            return high

        return -1