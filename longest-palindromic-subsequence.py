class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        newString = s[::-1]
        length = len(s)
        arr = [[0 for i in range(length+1)] for i in range(length+1)]

        for i in range(length-1,-1,-1):
            for j in range(length-1,-1,-1):
                if newString[i] == s[j]:
                    arr[i][j] += arr[i+1][j+1] + 1
                else:
                    arr[i][j] = max(arr[i+1][j],arr[i][j+1])

        return arr[0][0]