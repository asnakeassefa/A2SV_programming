class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_dict = defaultdict(int)
        s2_dict = defaultdict(int)
        m = len(s1)
        n = len(s2)

        if m > n:
            return False
        for char in s1:
            s1_dict[char] += 1

        for i in range(m):
            s2_dict[s2[i]] += 1
        
        if s2_dict == s1_dict:
            return True
        
        for i in range(n-m):
            s2_dict[s2[i]] -= 1
            s2_dict[s2[i+m]] += 1
            if s2_dict[s2[i]] == 0:
                s2_dict.pop(s2[i])
            if s2_dict == s1_dict:
                return True

        return False