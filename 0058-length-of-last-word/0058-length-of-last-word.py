class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        new = s.split(" ")
        i = -1
        while len(new[i]) == 0:
            i -= 1
        return len(new[i])