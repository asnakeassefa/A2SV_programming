class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        ans = []
        sumdict = defaultdict(int)
        sumdict[0] = 1
        Sum = 0
        ans = 0
        for num in nums:
            Sum += num
            case = Sum - goal
            ans += sumdict[case]
            sumdict[Sum] += 1
        return ans