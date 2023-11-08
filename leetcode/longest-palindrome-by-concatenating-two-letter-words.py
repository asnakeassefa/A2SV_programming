class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        odd = 0
        words = Counter(words)
        ans = 0
        for key,val in words.items():
            if key[0] == key[1]:
                if val % 2 == 1:
                    ans += (val - 1) * 2
                    odd += 1
                else:
                    ans += val * 2
            else:
                ans += min(words[key],words[key[::-1]]) * 2
        if odd:
            ans += 2
        return ans 