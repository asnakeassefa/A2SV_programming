class Solution:
    def getTime(self,piles,k):
        time = 0
        for pile in piles:
            if pile <= k:
                time += 1
            else:
                time += ceil(pile/k)
        return time
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)

        while low <= high:
            mid = low + (high - low) // 2
            if self.getTime(piles,mid) > h:
                low = mid + 1
            elif self.getTime(piles,mid) <= h:
                high = mid - 1
        
        return low