class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) < 5:
            return 0
        nums.sort()
        length = len(nums)
        points = [(3,length-1),(2,length-2),(1,length-3),(0,length-4)]
        ans = float("inf")
        for point in points:
            ans = min(ans,nums[point[1]] - nums[point[0]])
        return ans