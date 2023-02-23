class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        subarr = set()
        length = len(s)
        maxCount = 0
        
        right = 0
        left = 0
        
        ans = 0
        while right < length:
            if s[right] in subarr:
                subarr.remove(s[left])
                left += 1
                maxCount -= 1
            else:
                maxCount += 1
                subarr.add(s[right])
                right += 1
            ans = max(maxCount,ans)
        return ans