class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        store = defaultdict(int)
        length = len(nums)
        Max = 0
        for num in nums:
            Max = max(Max,abs(num))
        for i in range(length):
            nums[i] += Max

        for num in nums:
            i = 0
            while i < 32:
                store[i] += num & 1
                num >>= 1
                i += 1
        for i in range(33,-1,-1):
            ans <<= 1
            ans += store[i] % 3
        return ans - Max