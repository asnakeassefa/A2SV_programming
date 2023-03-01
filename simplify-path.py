class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        temp = ""
        count = 0
        for p in path:
            if p == "/":
                if count == 2 and len(temp) == 2:
                    if stack:
                        stack.pop()
                elif count == 1 and len(temp) == 1:
                    temp = ""
                    count = 0
                    continue
                else:
                    if len(temp) > 0:
                        stack.append("/"+temp)
                temp = ""
                count = 0
            else:
                temp += p
                if p == ".":
                    count += 1
        if temp:
            if not stack and temp != "." and temp != "..":
                stack.append("/" + temp)
            elif stack and temp != "." and temp != "..":
                stack.append("/"+temp)
            elif temp == ".." and stack:
                stack.pop()
        if not stack:
            stack.append("/")
        return "".join(stack)