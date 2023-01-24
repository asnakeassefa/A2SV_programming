class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        length = len(arr)
        ptr1 = 0
        ptr2 = length -1
        
        for i in range(1,length):
            if arr[i-1] >= arr[i]:
                ptr1 = i-1
                break
        for i in range(length-2,-1,-1):
            if arr[i] <= arr[i+1]:
                ptr2 = i+1
                break
        return length > 2 and ptr1 == ptr2