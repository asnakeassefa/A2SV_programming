class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        memo = defaultdict(int)

        for val in arr:
            memo[val] = memo[val-difference] + 1

        return max(memo.values())