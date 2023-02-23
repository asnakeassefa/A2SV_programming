class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        presum = defaultdict(int)
        Sum = 0
        presum[Sum] = 1
        ans = 0
        for num in nums:
            Sum += num
            case = Sum - k
            ans += presum[case]
            presum[Sum] += 1
        return ans