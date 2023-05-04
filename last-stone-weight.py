class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        result = list(map(lambda x: x * -1, stones))
        heapq.heapify(result)
        while result:
            if len(result) == 1:
                return result[0] * -1
            y = heappop(result)
            x = heappop(result)
            if x != y:
                heappush(result,y-x)
        return 0