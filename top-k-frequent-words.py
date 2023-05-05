class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        newWords = Counter(words)
        heaped = []
        for key,val in newWords.items():
            heaped.append((-val,key))
        heapify(heaped)
        ans = []
        for i in range(k):
            ans.append(heapq.heappop(heaped)[1])
        return ans