class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        size = max(trips,key = lambda x:x[2])[2] + 2
        newArray = [0] * size
        
        for trip in trips:
            newArray[trip[1]] += trip[0]
            newArray[trip[2]] -= trip[0]
        
        for i in range(1,size):
            newArray[i] += newArray[i-1]
        # print(newArray)
        if max(newArray) > capacity:
            return False
        else:
            return True