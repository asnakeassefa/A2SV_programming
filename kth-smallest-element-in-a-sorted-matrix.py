class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        lenCol = len(matrix[0])
        newArray = []
        heapq.heapify(newArray)
        for i,row in enumerate(matrix):
            for j,col in enumerate(row):
                if len(newArray) < k:
                    heapq.heappush(newArray,-col)
                else:
                    if newArray[0] < -col:
                        heapq.heappushpop(newArray,-col)
        
        return -newArray[0]