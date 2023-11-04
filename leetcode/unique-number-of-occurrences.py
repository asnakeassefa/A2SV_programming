class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = Counter(arr)

        length = len(set(count.values()))

        if len(count) == length:
            return True
        return False