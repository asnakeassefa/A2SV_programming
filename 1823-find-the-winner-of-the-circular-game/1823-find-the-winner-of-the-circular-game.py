class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        array = []
        for i in range(1,n+1):
            array.append(i)
        change = k - 1
        # removing elements
        num = 0
        while len(array) > 1:
            num += change
            while num >= len(array):
                num = num - len(array)
                
            array.pop(num)
            
        return array[0]