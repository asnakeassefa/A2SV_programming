class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def check(value):
            stack = []
            for val in value:
                if val == ')':
                    if not stack:
                        return False
                    else:
                        stack.pop()
                else:
                    stack.append('(')
            if stack:
                return False
            return True
        ans = set()
        def rec(value):
            if len(value) == n*2:
                if check(value):
                    ans.add(value)
                    return
            if len(value) > n*2:
                return
            
            rec(value + '(')
            rec(value + ')')
        rec("")
        return ans
                            