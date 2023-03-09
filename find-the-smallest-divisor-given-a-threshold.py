class Solution:
    def getSum(self,nums,d):
        res = 0
        for num in nums:
            res += ceil(num/d)
        return res
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        low = 1
        high = max(nums)

        while low <= high:
            mid = low + (high - low) // 2

            if self.getSum(nums,mid) > threshold:
                low = mid + 1
            else:
                high = mid - 1
        return low