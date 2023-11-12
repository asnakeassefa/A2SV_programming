class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        store = {}
        taken = set()
        for i,char in enumerate(s):
            if char not in store:
                if t[i] in taken:
                    return False
                store[char] = t[i]
                taken.add(t[i])
            elif store[char] != t[i]:
                return False
        return True