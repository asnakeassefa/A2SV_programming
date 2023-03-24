class Solution:
    def maxLength(self, arr: List[str]) -> int:
        sub = set("")
        ans = 0
        def backtrack(idx):
            nonlocal ans
            if len(sub) > 0:
                ans = max(ans,len("".join(sub)))
            if idx >= len(arr):
                return
            condition = True
            new = set()
            for char in arr[idx]:
                if char in sub or char in new:
                    condition = False
                    new = set()
                    break
                else:
                    new.add(char)
            if condition:
                for char in new:
                    sub.add(char)
                backtrack(idx+1)
                for char in new:
                    sub.remove(char)
            backtrack(idx+1)
        backtrack(0)
        return ans