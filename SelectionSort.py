#User function Template for python3

class Solution: 
    def select(self, arr, i):
        # code here
        return arr[i]
    
    def selectionSort(self, arr,n):
        #code here
        for x in range(len(arr) - 1):
            min_index = x
            for y in range(x+1,len(arr)):
                if arr[min_index] > arr[y]:
                    min_index = y
            
            temp = arr[min_index]
            arr[min_index] = arr[x]
            arr[x] = temp
        return arr
            
