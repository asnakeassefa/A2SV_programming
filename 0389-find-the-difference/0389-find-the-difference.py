class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        
        letters = []
        ans = ""
        # comping chars to list
        for string in t:
            letters.append(string)
        for string in s:
            letters.remove(string)
        for char in letters:
            ans += char
        return ans
            