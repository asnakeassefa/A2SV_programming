class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        counter = defaultdict(list)
        length = len(nums)
        for i,num in enumerate(nums):
            counter[num].append(i+1)
        maxlen = 1
        for val in counter.values():
            maxlen = max(maxlen,len(val))
        if maxlen == 1:
            return 1
        ans = [0,length-1]
        for key,val in counter.items():
            if len(val) == 1:
                continue
            if len(val) > ans[0]:
                ans[0] = len(val)
                ans[1] = val[-1] - val[0]
            elif len(val) == ans[0] and ans[1] > val[-1] - val[0]:
                ans[1] = val[-1] - val[0]
        return ans[1] + 1