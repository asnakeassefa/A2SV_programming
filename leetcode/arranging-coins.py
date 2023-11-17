class Solution:
    def arrangeCoins(self, n: int) -> int:
        
        low = 1
        high = n

        while low < high:
            mid = low + (high - low) // 2

            if mid * (mid+ 1) /2 < n:
                low = mid + 1
            else:
                high = mid
        if low * (low + 1) //2 > n:
            low -= 1
        return low