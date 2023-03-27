class Solution:
    def getPivot(self,nums,left,right):
        pivot  = nums[right]
        j = left - 1
        for i in range(left,right):
            if nums[i] <= pivot:
                j += 1
                nums[i],nums[j] = nums[j],nums[i]
        nums[j+1],nums[right] = nums[right],nums[j+1]
        return j+1
    def getK(self,nums,k,left,right):
        pivot = self.getPivot(nums,left,right)

        if pivot == k:
            return nums[pivot]
        elif pivot > k:
            ans = self.getK(nums,k,left,pivot-1)
        elif pivot < k:
            ans = self.getK(nums,k,pivot+1,right)
        return ans
    def findKthLargest(self, nums: List[int], k: int) -> int:
        ans = 3
        length = len(nums)
        ans = self.getK(nums,length-k,0,length-1)
        return ans