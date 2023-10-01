class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        length = len(satisfaction)
        values = [0] * (length+1)
        sum_p = 0

        for i in range(length-1,-1,-1):
            sum_p += satisfaction[i]
            values[i] = values[i+1] + sum_p
        return max(values)