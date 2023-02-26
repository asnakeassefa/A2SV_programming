class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        newSum = []
        presum = 0
        for num in nums:
            presum += num
            newSum.append(presum)
        return newSum