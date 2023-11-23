class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)
        length = len(nums)/3
        ans = []
        for key,val in counter.items():
            if val > length:
                ans.append(key)
        return ans