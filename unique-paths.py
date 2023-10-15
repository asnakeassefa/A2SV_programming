class Solution:
    def inbound(self,m,n,curr):
        return 0<=curr[0]<m and 0<=curr[1]<n

    def uniquePaths(self, m: int, n: int) -> int:
        length = (n-1) + (m-1)
        ans = math.factorial(length) // (math.factorial(n-1) * math.factorial(m-1))

        return ans