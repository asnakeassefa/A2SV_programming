class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        nums = [i+1 for i in range(n)]

        def backTrack(idx,arr):
            if len(arr) == k:
                ans.append(arr[:])
                return
            if idx == len(nums):
                return
            arr.append(nums[idx])
            backTrack(idx + 1,arr)
            arr.pop()
            backTrack(idx + 1,arr)
            
        backTrack(0,[])
        return ans