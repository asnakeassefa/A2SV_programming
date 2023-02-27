class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        ans = 0
        Sum = 0
        odds = defaultdict(int)
        odds[0] = 1
        length = len(nums)
        
        for i in range(length):
            if nums[i] % 2==0:
                nums[i] = 0
            else:
                nums[i] = 1
        
        ans = 0
        
        for num in nums:
            Sum += num
            case = Sum - k
            ans += odds[case]
            odds[Sum] += 1
        return ans