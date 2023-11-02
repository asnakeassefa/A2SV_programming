class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        length = len(arr)
        if length + k > arr[-1]:
            missed = arr[-1] - length
            k = k - missed
            return arr[-1] + k

        low = 0
        high = len(arr) - 1

        while low < high:
            mid = low + (high - low) // 2
            
            if arr[mid] - (mid + 1) < k:
                low = mid + 1
            else:
                high = mid
        missed = arr[low] - low
        val = (missed -k)
        return arr[low] - val