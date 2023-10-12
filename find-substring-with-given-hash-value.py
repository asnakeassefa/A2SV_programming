class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        alp = 'abcdefghijklmnopqrstuvwxyz'
        chars = defaultdict(int)
        #build index of alphabets
        for i,char in enumerate(alp):
            chars[char] = i+1
        #build for the last substring:
        val = 0
        length = len(s)
        j = k-1
        for i in range(length-1,length-(k+1),-1):
            val = (val + (chars[s[i]] * pow(power,j,modulo))) % modulo
            j -= 1
        val %= modulo
        #build the answer
        ans = j
        if val == hashValue:
            ans = length-(k)
        j = k-1
        p = pow(power,j,modulo)
        for i in range(length-(k+1),-1,-1):
            val = (((val - (chars[s[i+k]]) * p)*power ) + chars[s[i]]) % modulo
            if val == hashValue:
                ans = i

        return s[ans:ans+k]