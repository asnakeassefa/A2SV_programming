class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        def kmp(pattern,text):
            m = len(pattern)
            n = len(text)
            lsp = [0] * m
            j = 0
            for i in range(1,m):
                while j > 0 and pattern[i] != pattern[j]:
                    j = lsp[j-1]
                if pattern[i] == pattern[j]:
                    j += 1
                lsp[i] = j

            j = 0
            i = 0
            count = 0
            while j < m:
                if j == 0 and i == (n-1) and text[i] != pattern[j]:
                    return -1
                while j > 0 and text[i] != pattern[j]:
                    if count > 1:
                        return -1
                    j = lsp[j-1]
                if text[i] == pattern[j]:
                    j += 1
                if j == m:
                    return count + 1
                i += 1
                if i == n:
                    count += 1
                i %= n
            return count + 1
  
        return kmp(b,a)