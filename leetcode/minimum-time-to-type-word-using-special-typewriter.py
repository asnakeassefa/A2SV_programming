class Solution:
    def minTimeToType(self, word: str) -> int:
        letters = 'abcdefghijklmnopqrstuvwxyz'
        ans = 0
        curr = 0
        for char in word:
            ptr = 0
            while letters[(curr - ptr) % 26] != char and letters[(curr + ptr) % 26] != char:
                ptr += 1
            if letters[(curr - ptr) % 26] == char:
                curr = (curr - ptr) % 26
            elif letters[(curr + ptr) % 26] == char:
                curr = (curr + ptr) % 26
            ans += ptr +1
        return ans
            