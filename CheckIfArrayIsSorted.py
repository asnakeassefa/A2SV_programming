#User function Template for python3

class Solution:
    def arraySortedOrNot(self, arr, n):
        for i in range(1,n):
            if arr[i-1] > arr[i]:
                return 0
        return 1
