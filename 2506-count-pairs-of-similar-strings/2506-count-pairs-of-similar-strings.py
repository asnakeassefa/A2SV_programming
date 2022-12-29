class Solution:
    #define a function which compair two words
    def compair(self,word1,word2):
        set1 = set()
        set2 = set()
        for word in word1:
            set1.add(word)
        for word in word2:
            set2.add(word)
        if set1 == set2:
            return True
    def similarPairs(self, words: List[str]) -> int:
        ans = 0
        for index,word in enumerate(words):
            for val in words[index+1:]:
                if set(word) == set(val):
                    ans += 1
        return ans