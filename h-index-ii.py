class Solution:
    def hIndex(self, citations: List[int]) -> int:
        length = len(citations)
        low = 0
        high = length - 1

        while low <= high:
            mid = low + (high - low)//2
            if citations[mid] < length-mid:
                low = mid + 1
            elif citations[mid] >= length-mid:
                high = mid - 1
        
        return length - low