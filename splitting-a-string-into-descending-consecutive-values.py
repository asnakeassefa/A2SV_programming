class Solution:
    def splitString(self, s: str) -> bool:
        arr = []

        def backtrack(idx):
            if idx == len(s):
                return len(arr) >= 2
            
            for i in range(idx,len(s)):
                value = int(s[idx:i+1])

                if not arr or value == arr[-1] -1:
                    arr.append(value)
                    if backtrack(i + 1):
                        return True
                    arr.pop()
            return False
        return backtrack(0)