class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ans = 1
        curr = 1
        prev = 0
        length = len(nums)
        while curr < length:
            if nums[prev] < nums[curr]:
                ans += 1
                prev += 1
                nums[prev] = nums[curr]
            curr += 1
            
        return ans