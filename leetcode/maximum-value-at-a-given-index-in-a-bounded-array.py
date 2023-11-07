class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        def getSum(value):
            leftTotal , rightTotal = 0,0
            left = index
            right = n-1-index
            #left
            if value > left:
                leftTotal += value * (value+1)//2
                temp = value - left
                leftTotal -= temp * (temp+1)//2
            else:
                leftTotal += value * (value+1)//2
                leftTotal += left-value

            #right
            if value > right:
                rightTotal += value * (value+1)//2
                temp = value - right
                rightTotal -= temp * (temp+1)//2
            else:
                rightTotal += value * (value+1)//2
                rightTotal += right-value
            
            return rightTotal + leftTotal

        low = 1
        high = maxSum

        while low < high:
            mid = low + (high-low)//2
            if getSum(mid-1) + mid < maxSum:
                low = mid + 1
            else:
                high = mid

        res = getSum(low-1) + low
        return low if res <= maxSum else low-1

