class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        Max = 0
        length = len(nums)
        ans = 0
        store = set()
        for num in nums:
            Max |= num
        temp = []
        def backtrack(idx,innerMax):
            nonlocal ans
            if Max == innerMax and tuple(temp) not in store:
                store.add(tuple(temp))
                ans += 1
            if idx >= length:
                return
            
            temp.append((nums[idx],idx))
            backtrack(idx + 1,innerMax | nums[idx])
            temp.pop()
            backtrack(idx + 1,innerMax)

        backtrack(0,0)
        return ans