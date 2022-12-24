class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        ans = -1
        minVal = float('inf')
        
        for index, point in enumerate(points):
            if x == point[0] and y == point[1]:
                return index
            elif x == point[0]:
                val = abs(point[1]-y)
                if minVal > val:
                    ans = index
                    minVal = val
            elif y == point[1]:
                val = abs(point[0]-x)
                if minVal > val:
                    ans = index
                    minVal = val
            else:
                continue
        
        if minVal == float('inf'):
            return ans
        
        return ans