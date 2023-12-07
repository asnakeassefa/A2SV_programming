class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ptr = 0
        length = len(s)
        for char in t:
            if length == ptr:
                return True
            if char == s[ptr]:
                ptr += 1
        if length == ptr:
            return True
        return False