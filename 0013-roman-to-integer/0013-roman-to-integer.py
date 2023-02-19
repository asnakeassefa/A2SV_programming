class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {"I":1 , "V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        s = s[::-1]
        print(s)
        ptr =  1
        ans = dic[s[0]]
        length = len(s)
        while ptr < length:
            if dic[s[ptr]] < dic[s[ptr-1]]:
                ans -= dic[s[ptr]]
            else:
                ans += dic[s[ptr]]
            ptr += 1
        return ans