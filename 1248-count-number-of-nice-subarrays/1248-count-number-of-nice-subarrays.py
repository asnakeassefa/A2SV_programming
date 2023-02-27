class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        ans = 0
        Sum = 0
        odds = defaultdict(int)
        odds[0] = 1
        length = len(nums)
        ans = 0
        for num in nums:
            Sum += num % 2
            case = Sum - k
            ans += odds[case]
            odds[Sum] += 1
        return ans