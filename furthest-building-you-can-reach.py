class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        values = [0]
        heapq.heapify(values)
        length = len(heights)
        diff = [0]
        Sum = 0
        counter = 0
        for i in range(length-1):
            val = heights[i+1] - heights[i]
            if val <= 0:
                diff.append(0)
            else:
                diff.append(val)
        print(diff)
        ans = 0
        for i,val in enumerate(diff):
            ans = i
            heapq.heappush(values,-val)
            Sum += val

            if Sum > bricks and ladders == 0:
                return ans - 1
                break
            
            if Sum > bricks and ladders:
                temp = heapq.heappop(values)
                Sum += temp
                ladders -= 1
        return ans