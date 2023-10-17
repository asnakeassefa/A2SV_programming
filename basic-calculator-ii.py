class Solution:
    def calculate(self, s):
        size = len(s)
        stack = []
        num = 0
        opr = '+'
        i = 0
        
        while i < size:
            ch = s[i]
            if ch.isdigit():
                num = num * 10 + int(ch)
            
            if (not ch.isdigit() and not ch.isspace()) or i == size - 1:
                if opr == '-':
                    stack.append(-num)
                elif opr == '+':
                    stack.append(num)
                elif opr == '*':
                    stack.append(stack.pop() * num)
                elif opr == '/':
                    stack.append(int(stack.pop() / num))
                opr = ch
                num = 0
            
            i += 1
        
        result = 0
        for value in stack:
            result += value
        
        return result