class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = [("A",0)]

        length = len(s)
        for i in range(1,length+1):
            if stack[-1][0] == s[i-1]:
                stack.append((s[i-1],stack[-1][1]+1))
            else:
                stack.append((s[i-1],1))
            while stack[-1][1] == k:
                for i in range(k):
                    stack.pop()
        ans = ""
        length = len(stack)
        for i in range(1,length):
            ans += stack[i][0]
        return ans