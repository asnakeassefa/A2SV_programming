class Solution:
    def partitionString(self, s: str) -> int:
        count = defaultdict(int)
        ans = 0
        for char in s:
            if count[char]:
                ans += 1
                count = defaultdict(int)
            count[char] += 1
        return ans + 1