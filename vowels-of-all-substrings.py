class Solution:
    def countVowels(self, word: str) -> int:
        vowels = {'a','e','i','o','u'}
        ans = 0
        n = len(word)
        for i,char in enumerate(word):
            if char in vowels:
                ans += (1+i) * (n-i)

        return ans