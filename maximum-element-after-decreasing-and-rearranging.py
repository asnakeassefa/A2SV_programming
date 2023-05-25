class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort(reverse = True)
        count = 0
        while arr:
            value = arr.pop()
            if value > count:
                count += 1
        return count