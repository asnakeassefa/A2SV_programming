class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        length = len(names)
        for i in range(length):
            for j in range(length-1-i):
                if heights[j] < heights[j+1]:
                    heights[j],heights[j+1] = heights[j+1],heights[j]
                    names[j],names[j+1] = names[j+1],names[j]
        
        return names
        