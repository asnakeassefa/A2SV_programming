class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operator = {"+","-","/","*"}
        stack = []
        ans = 0
        for token in tokens:
            if token in operator:
                if token == "+":
                    ans = stack.pop() + stack.pop()
                    stack.append(ans)
                elif token == "-":
                    num1 = stack.pop()
                    num2 = stack.pop()
                    ans = num2 - num1
                    stack.append(ans)
                elif token == "/":
                    num1 = stack.pop()
                    num2 = stack.pop()
                    ans = num2 / num1
                    stack.append(int(ans))
                elif token == "*":
                    ans = stack.pop() * stack.pop()
                    stack.append(int(ans))
            else:
                stack.append(int(token))
        return stack[-1]