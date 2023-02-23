class NumArray:

    def __init__(self, nums: List[int]):
        self.presum = [0]
        for num in nums:
            self.presum.append(num + self.presum[-1])

    def sumRange(self, left: int, right: int) -> int:
        ans = self.presum[right+1] - self.presum[left]
        return ans
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)