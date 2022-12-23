class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        length1 = len(word1)
        length2 = len(word2)
        ans = ""
        length = min(length1,length2)
        
        for i in range(length):
            ans += word1[i]
            ans += word2[i]
        if length == length1:
            ans += word2[length:]
        elif length == length2:
            ans += word1[length:]
            
        return ans