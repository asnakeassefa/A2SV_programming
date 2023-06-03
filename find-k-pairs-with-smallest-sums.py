class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        maxHeap = []
        ans = []
        for num1 in nums1:
            for num2 in nums2:
                val = -(num1+num2)
                if len(maxHeap) < k:
                    heapq.heappush(maxHeap,[val,[num1,num2]])
                else:
                    if val < maxHeap[0][0]:
                        break
                    heapq.heappop(maxHeap)
                    heapq.heappush(maxHeap,[val,[num1,num2]])

        for i in range(k):
            if maxHeap:
                ans.append(heapq.heappop(maxHeap)[1])
        return ans