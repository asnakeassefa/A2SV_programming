class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        length = len(needle)
        length2 = len(haystack)
        if length > length2:
            return -1
        idx = defaultdict()
        alp = "abcdefghijklmnopqrstuvwxyz"
        # build index
        for i,char in enumerate(alp):
            idx[char] = i

        j = length - 1
        val = 0
        # build for first string
        needleVal = 0
        for i in range(length):
            val += idx[haystack[j]] * (26 ** i)
            needleVal += idx[needle[j]] * (26 ** i)
            j -= 1
        start = val % (10 ** 9 + 7)
        needleVal %= (10 ** 9 + 7)
        if start == needleVal:
            return 0
        for i in range(1,length2-(length-1)):
            val -= (26**(length-1) * idx[haystack[i-1]])
            val *= 26
            val += idx[haystack[i + length-1]]
            if needleVal == val % (10 ** 9 + 7):
                return i
        
        return -1