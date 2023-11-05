class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = Counter(nums)
        ans = 0
        for val in count.values():
            ans += math.comb(val,2)
        return ans