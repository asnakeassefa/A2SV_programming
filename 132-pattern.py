class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        # ans = False
        length = len(nums)
        for num in nums:
            if not stack:
                stack.append((num,num))
                Min = num
            Min = min(Min,num)
            while stack and stack[-1][0] < num:
                stack.pop()
            if stack and stack[-1][1] < num < stack[-1][0]:
                return True
            stack.append((num,Min))
        return False