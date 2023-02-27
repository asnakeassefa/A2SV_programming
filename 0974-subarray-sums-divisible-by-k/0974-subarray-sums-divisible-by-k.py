class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        
        length = len(nums)
        sumDict = defaultdict(int)
        sumDict[0] = 1
        ans = 0
        Sum = 0
        for num in nums:
            Sum += num
            case = Sum % k
            ans += sumDict[case]
            sumDict[Sum%k] += 1
        
        return ans