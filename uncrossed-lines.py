class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        length1 = len(nums1)
        length2 = len(nums2)
        arr = [[0 for i in range(length2+1)] for i in range(length1+1)]

        for i in range(length1-1,-1,-1):
            for j in range(length2-1,-1,-1):
                if nums1[i] == nums2[j]:
                    arr[i][j] += arr[i+1][j+1] + 1
                else:
                    arr[i][j] = max(arr[i+1][j],arr[i][j+1])
        
        return arr[0][0]