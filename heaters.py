class Solution:
    def check(self,rad,houses,heaters):
        ans = False
        j = 0
        i = 0
        length = len(houses)
        length2 = len(heaters)
        while i < length and j < length2:
            if abs(houses[i]-heaters[j]) <= rad:
                i += 1
            else:
                j += 1
                if j == length2:
                    return False
        return True
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        houses.sort()
        low = 0
        high = max(houses[-1]-heaters[0], heaters[-1] - houses[0])

        while low < high:
            mid = low + (high-low)//2
            if not self.check(mid,houses,heaters):
                low = mid + 1
            else:
                high = mid

        return low

        return 1