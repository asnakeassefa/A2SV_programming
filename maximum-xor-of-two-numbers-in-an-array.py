class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        length = len(nums)
        newNums = []
        for i in range(length):
            newNums.append(bin(nums[i])[2:].zfill(32))
        mask = 0
        ans = 0
        for i in range(31,-1,-1):
            store = set()
            mask |= (1<<i)
            for num in nums:
                store.add(num & mask)
            temp = ans | (1<<i)
            for val in store:
                if val ^ temp in store:
                    ans |= (1<<i)
                    break
        return ans