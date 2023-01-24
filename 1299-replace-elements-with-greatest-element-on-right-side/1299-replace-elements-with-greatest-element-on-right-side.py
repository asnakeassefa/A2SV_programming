class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        length = len(arr)
        ans = []
        for i in range(length-1,-1,-1):
            if i == length-1:
                ans.append(-1)
                temp = arr[i]
            else:
                ans.append(temp)
            temp = max(temp,arr[i])
        ans.reverse()
        return ans