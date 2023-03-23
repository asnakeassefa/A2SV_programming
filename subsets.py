class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        arr = []
        memo = defaultdict(int)
        length = len(nums)

        def backtrack(idx):
            if idx >= length:
                ans.add(tuple(arr[:]))
                return
            for i in range(idx,length):
                arr.append(nums[i])
                backtrack(i+1)
                arr.pop()
            backtrack(idx+1)
        backtrack(0)
        return ans