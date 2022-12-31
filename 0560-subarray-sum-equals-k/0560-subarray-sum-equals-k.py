class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        SUM = 0
        dic = defaultdict(int)
        dic[0] = 1
        ans = 0
        for num in nums:
            SUM += num
            ans += dic[SUM - k]
            dic[SUM] += 1
        return ans