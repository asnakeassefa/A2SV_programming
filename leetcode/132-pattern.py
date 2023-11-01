class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        length = len(nums)
        Min = float('inf')
        for num in nums:
            Min = min(Min,num)
            while stack and stack[-1][0] < num:
                stack.pop()
            if stack and stack[-1][1] < num < stack[-1][0]:
                return True
            stack.append((num,Min))
        return False