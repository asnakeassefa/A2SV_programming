class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1len = len(s1)
        s2len = len(s2)
        if len(s1) > len(s2):
            return False
        
        s1dict = defaultdict(int)
        s2dict = defaultdict(int)
        
        for i in range(s1len):
            s1dict[s1[i]] += 1
            s2dict[s2[i]] += 1
        if s1dict == s2dict:
            return True
        left = 0
        
        for i in range(s1len,s2len):
            s2dict[s2[i]] += 1
            s2dict[s2[left]] -= 1
            
            if s2dict[s2[left]] == 0:
                s2dict.pop(s2[left])
            left += 1
            if s2dict == s1dict:
                return True
        return False
            