#User function Template for python3

class Solution:
    #Heapify function to maintain heap property.
    def heapify_up(self,arr,i):
        # code here
        parent = (i - 1)//2
        if arr[i] > arr[parent] and i:
            arr[i],arr[parent] = arr[parent],arr[i]
            self.heapify_up(arr,parent)
    def heapify_down(self,arr,n,curr):
        Max_val = curr
        left = curr * 2 + 1
        right = curr * 2 + 2
        
        if left < n and arr[left] > arr[Max_val]:
            Max_val = left
        if right < n and arr[right] > arr[Max_val]:
            Max_val = right
        
        if arr[Max_val] != arr[curr]:
            arr[Max_val],arr[curr] = arr[curr],arr[Max_val]
            self.heapify_down(arr,n,Max_val)
    #Function to build a Heap from array.
        
    def buildHeap(self,arr,n):
        # # code here
        newarr = [arr[0]]
        for i,val in enumerate(arr):
            if i == 0:
                continue
            newarr.append(val)
            self.heapify_up(newarr,len(newarr)-1)
        return newarr
    #Function to sort an array using Heap Sort.    
    def HeapSort(self, arr, n):
        #code here
        length = len(arr)
        values = self.buildHeap(arr,len(arr))
        for i,val in enumerate(values):
            arr[i] = val
        i = 1
        while i < len(arr):
            arr[0],arr[length-i] = arr[length-i],arr[0]
            self.heapify_down(arr,length-i,0)
            i += 1
#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Mohit Kumara

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().HeapSort(arr,n)
        print(*arr)

# } Driver Code Ends