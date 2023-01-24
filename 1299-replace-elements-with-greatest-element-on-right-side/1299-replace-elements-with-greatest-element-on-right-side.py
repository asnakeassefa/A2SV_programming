class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        length = len(arr)
        
        for i in range(length-1,-1,-1):
            if i == length-1:
                temp = arr[i]
                arr[i] = -1
            else:
                temp1 = arr[i]
                arr[i] = temp
                temp = max(temp,temp1)
        return arr