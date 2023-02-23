class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        pivot = -1
        temp = 0
        length = len(nums)
        presum = [0]
        # building presum
        for num in nums:
            temp += num
            presum.append(temp)
        # finding the pivot
        for i in range(1,length+1):
            if presum[i-1] == presum[-1] - presum[i]:
                pivot = i-1
                break
        return pivot