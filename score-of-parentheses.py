class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        temp = []
        lastLen = 0
        length = len(s)
        for i,char in enumerate(s):
            if char != ")":
                stack.append(char)
            else:
                while stack[-1] != "(":
                    temp.append(int(stack.pop()))
                stack.pop()
                if len(temp) == 0:    
                    newVal = 1
                    if stack and stack[-1] != "(":
                        stack.append(stack.pop() + newVal)
                    else:
                        stack.append(newVal)
                elif len(temp) == 1:
                    newVal = 2*temp[0]
                    if stack and stack[-1] != "(":
                        stack.append(stack.pop() + newVal)
                    else:
                        stack.append(newVal)
                    temp = []
                elif len(temp) > 1:
                    newVal = sum(temp)
                    if stack and stack[-1] != "(":
                        stack.append(stack.pop() + newVal)
                    else:
                        stack.append(newVal)
                    temp = []
            print(stack)
        return sum(stack)