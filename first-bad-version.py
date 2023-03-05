# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        right = n-1
        left = 0
        while left <= right:
            mid = left + (right-left)//2
            if isBadVersion(mid):
                right = mid-1
            elif not isBadVersion(mid):
                left = mid + 1
        return left