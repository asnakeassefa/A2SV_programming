class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 0
        length = len(s)
        ans = 0
        
        subArray = defaultdict(int)
    
        for right in range(length):
            subArray[s[right]] += 1
            most_freq = max(subArray.values())
            
            if right - left + 1 - most_freq > k:
                subArray[s[left]] -= 1
                left += 1
        
        return length - left