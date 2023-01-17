class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        length = len(names)
        for i in range(length):
            minindex = i
            for j in range(i+1,length):
                if heights[j] > heights[minindex]:
                    minindex = j
            heights[minindex],heights[i] = heights[i],heights[minindex]
            names[minindex],names[i] = names[i],names[minindex]
        
        return names
        