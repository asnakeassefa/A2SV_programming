class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 0
        length = len(s)
        ans = 0
        
        subArray = defaultdict(int)
        subArray[s[right]] += 1
        right += 1
        # iteratring through the string
        while right < length:
            temp = max(subArray.values())
            if (right- left) - temp > k:
                MAX = temp + k
                ans = max(ans,MAX)
                subArray[s[left]] -= 1
                left += 1
            else:
                subArray[s[right]] += 1
                right += 1
        temp = max(subArray.values()) + k
        if temp > length:
            ans = length
        else:
            ans = max(ans,temp)
        return ans