class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        ans = set()
        
        for num in nums:
            ans.add(num)
            temp = str(num)
            temp = int(temp[::-1])
            ans.add(temp)
        return len(ans)