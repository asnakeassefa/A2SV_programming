class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        ans = 0
        length = len(piles)
        piles.sort(reverse = True)
        i = 1
        count = 0
        while i < length:
            ans += piles[i]
            count += 1
            i += 2
            if count == length //3:
                break
        return ans