class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        max_ = max(nums)
        min_ = min(nums)

        if (max_ - k) - (min_ + k) < 0:
            return 0
        else:
            return (max_ - k) - (min_ + k)