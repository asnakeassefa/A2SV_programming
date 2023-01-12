class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        ans = []
        commentStarted = False
        for code in source:
            ptr1 = 0
            ptr2 = 1
            length = len(code)
            if not commentStarted:
                temp = ""
            if not commentStarted and length == 1:
                temp = code
            while ptr2 < length:
                if commentStarted:
                    if code[ptr1] == '*' and code[ptr2] == '/':
                        commentStarted = False
                        ptr1 += 2
                        ptr2 += 2
                        if ptr2 == len(code):
                            temp += code[ptr1]
                    else:
                        ptr1 += 1
                        ptr2 += 1
                else:
                    if code[ptr1] == '/' and code[ptr2] == '/':
                        break
                    elif code[ptr1] == '/' and code[ptr2] == '*':
                        commentStarted = True
                        ptr1 += 2
                        ptr2 += 2
                    elif not commentStarted:
                        temp += code[ptr1]
                        ptr1 += 1
                        ptr2 += 1
                    else:
                        ptr1 += 1
                        ptr2 += 1
                    
                    if ptr2 >= len(code):
                        temp += code[ptr1]
            
            if not commentStarted and len(temp) > 0:
                ans.append(temp)
        
        return ans