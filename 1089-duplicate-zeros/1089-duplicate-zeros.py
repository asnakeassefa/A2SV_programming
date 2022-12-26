class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        length = len(arr)
        i = 0
        while i < length:
            if arr[i] == 0:
                arr.insert(i,0)
                arr.pop()
                i += 1
            i += 1
        