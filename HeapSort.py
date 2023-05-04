#User function Template for python3

class Solution:
    #Heapify function to maintain heap property.
    def heapify(self,arr,n):
        # code here
        starting = (len(arr)//2) - 1
        for i in range(starting,-1,-1):
            self.heapify_down(arr,n,i)
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
        self.heapify(arr,len(arr))
    #Function to sort an array using Heap Sort.    
    def HeapSort(self, arr, n):
        #code here
        length = len(arr)
        self.buildHeap(arr,length)
        # print(arr)
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