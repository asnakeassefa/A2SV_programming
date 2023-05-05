class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        newPiles = list(map(lambda x:-x,piles))
        heapq.heapify(newPiles)

        for _ in range(k):
            val = heapq.heappop(newPiles)
            val = val//2
            heapq.heappush(newPiles,val)

        return -(sum(newPiles))