from sortedcontainers import SortedSet
class Solution:
    def minAbsoluteDifference(self, nums: List[int], x: int) -> int:
        sortedArr = SortedSet()
        ans = float('inf')
        for i,num in enumerate(nums):
            if num in sortedArr:
                return 0
            if i - x >= 0:
                sortedArr.add(nums[i-x])
            if sortedArr:
                right = min(bisect_right(sortedArr,num),len(sortedArr)-1)
                left = max(right-1,0)
                ans = min(ans,abs(num-sortedArr[left]),abs(num-sortedArr[right]))
        
        return ans
