class Solution:
    def ipv4(self,strings):
        chars = set(['1','2','3','4','5','6','7','8','9','0'])
        for val in strings:
            print(val)
            if len(val) > 3 or len(val) == 0:
                return False
            for char in val:
                if char not in chars:
                    return False
            if len(val) > 1 and val[0] == '0':
                return False
            if -1 < int(val) > 255:
                return False
        return True
    def ipv6(self,strings):
        chars = set(['1','2','3','4','5','6','7','8','9','0','A','B','C','D','E','F','a','b','c','d','e','f',':'])
        for val in strings:
            if len(val) > 4 or len(val) == 0:
                return False
            for char in val:
                if char not in chars:
                    return False
        return True
    def validIPAddress(self, queryIP: str) -> str:
        val1 = list(queryIP.split("."))
        val2 = list(queryIP.split(":"))
        
        if len(val1) == 4:
            print(val1)
            if self.ipv4(val1):
                return "IPv4"
        elif len(val2) == 8:
            if self.ipv6(val2):
                return "IPv6"
        return "Neither"