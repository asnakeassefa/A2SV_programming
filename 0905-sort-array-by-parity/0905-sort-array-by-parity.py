class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        
        even = []
        odd = []
        length = len(nums)
        nums.sort()
        # copying all even numbers
        for num in nums:
            if num %2 == 0:
                even.append(num)
            elif num %2 != 0:
                odd.append(num)
        return even + odd
        