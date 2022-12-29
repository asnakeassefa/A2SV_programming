class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        temp = []
        ans = ""
        notEqual = False
        for char in strs[0]:
            temp.append(char)
        
        length = len(temp)
        for chars in strs:
            if len(chars) < length:
                length = len(chars)
        
        temp = temp[:length]
        
        i = 0
        while i < length:
            for chars in strs:
                if temp[i] != chars[i]:
                    temp = temp[:i]
                    notEqual = True
                    break
            if notEqual:
                break
            i += 1
        print(temp)
        ans = "".join(temp)
        
        return ans