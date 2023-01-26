class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        countTarget = 0
        countsmall = 0
        ans = []
        for num in nums:
            if num < target:
                countsmall += 1
            elif num == target:
                countTarget += 1
                
        for i in range(countTarget):
            ans.append(countsmall + i)
            
        return ans