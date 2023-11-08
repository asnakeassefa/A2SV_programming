class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ans = False
        length = len(matrix[0])
        for row in matrix:
            low = 0
            high = length-1
            while low < high:
                mid = low + (high - low)//2
                if row[mid] < target:
                    low = mid + 1
                else:
                    high = mid
            if row[low] == target:
                return True
            # if row < length and row[low] == target
            #     row[low-1] == target:
            #     return True
        return False