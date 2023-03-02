class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        length = len(nums)
        stack = []
        stackdict = defaultdict(lambda: -1)
        getMax = -float('inf')
        maxIndex = 0
        for i in range(length):
            if getMax < nums[i]:
                getMax = nums[i]
                maxIndex = i
        nums = nums[maxIndex+1:] + nums[:maxIndex+1]
        
        for i,num in enumerate(nums):
            if not stack:
                stack.append((num,i))
            else:
                if stack[-1][0] >= num:
                    stack.append((num,i))
                else:
                    while stack and stack[-1][0] < num:
                        stackdict[stack.pop()] = num
                    stack.append((num,i))
        for i in range(length-1):
            nums[i] = stackdict[(nums[i],i)]
        nums[-1] = -1
        sep = length-maxIndex-1
        nums = nums[sep:]+nums[:sep]
        return nums