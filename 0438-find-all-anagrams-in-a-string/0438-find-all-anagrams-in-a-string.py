class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        target = defaultdict(int)
        window = defaultdict(int)
        for char in alphabet:
            target[char] = 0
            window[char] = 0
        for char in p:
            target[char] += 1
        length = len(s)
        length2 = len(p)
        if length2 > length:
            return []
        for i in range(length2):
            window[s[i]] += 1
        anagram = []
        if target == window:
            anagram = [0]
        
        left = 0
        right = length2
        
        while right < length:
            window[s[left]] -= 1
            window[s[right]] += 1
            left += 1
            right += 1
            if window == target:
                anagram.append(left)
        
        return anagram