class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        length = len(arr)
        ans = []
        arr.reverse()
        for i in range(length):
            if i == 0:
                ans.append(-1)
                temp = arr[i]
            else:
                ans.append(temp)
            temp = max(temp,arr[i])
        ans.reverse()
        return ans