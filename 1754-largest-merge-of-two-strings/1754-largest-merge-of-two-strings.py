class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        word1 = list(word1)
        word2 = list(word2)
        ans = ""
        while word1 and word2:
            if word1 >= word2:
                ans += word1.pop(0)
            else:
                ans += word2.pop(0)
        if word1:
            ans += ''.join(word1)
        if word2:
            ans += ''.join(word2)
            
        return ans