class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) > len(s3):
            return False
        @cache
        def dp(ptr1,ptr2):
            if ptr1 + ptr2 >= len(s3):
                return True
            res = False
            if ptr1 < len(s1) and s1[ptr1] == s3[ptr1 + ptr2]:
                res = res or dp(ptr1 + 1,ptr2)
            if ptr2 <len(s2) and s2[ptr2] == s3[ptr1 + ptr2]:
                res = res or dp(ptr1,ptr2 + 1)
            return res
        return dp(0,0)