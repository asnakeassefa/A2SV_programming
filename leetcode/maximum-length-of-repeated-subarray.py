class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        row = len(nums1)
        col = len(nums2)
        dp = [[0 for i in range(col+1)] for i in range(row+1)]

        for i in range(row-1,-1,-1):
            for j in range(col-1,-1,-1):
                if nums1[i] == nums2[j]:
                    dp[i][j] += dp[i+1][j+1] + 1
                else:
                    dp[i][j] = 0
        ans = 0
        for row in dp:
            ans = max(ans,max(row))

        return ans