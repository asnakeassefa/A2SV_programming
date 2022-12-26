class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        counter = nums.count(val)
        
        for i in range(counter):
            nums.remove(val)
        ans = len(nums)   
        return ans