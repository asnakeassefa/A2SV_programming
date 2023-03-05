class Solution:
    def mySqrt(self, x: int) -> int:
        right = x+1
        left = 0

        while left <= right:
            mid = left + (right-left)//2
            if mid * mid > x:
                right = mid - 1
            elif mid * mid < x:
                left = mid + 1
            else:
                return mid
        return left -1