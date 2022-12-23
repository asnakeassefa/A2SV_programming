class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        
        letters = []
        ans = ""
        # compering chars to list
        for string in t:
            letters.append(string)
        # removing elements form t   
        for string in s:
            letters.remove(string)
        
        return letters[0]