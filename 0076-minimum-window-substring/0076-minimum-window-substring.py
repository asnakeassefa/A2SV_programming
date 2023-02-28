class Solution:
    def minWindow(self, s: str, t: str) -> str:
        length = len(s)
        matched = 0
        
        subArray = defaultdict(int)
        target = defaultdict(int)
        
        for char in t:
            target[char] += 1
        
        targetLength = len(target)
        ans = ""
        left = 0
        minright = float('inf')
        minleft = 0
        
        for right in range(length):
            subArray[s[right]] += 1
            
            if subArray[s[right]] == target[s[right]]:
                matched += 1
                # print(minright,minleft)
            # print(matched,targetLength)
            while matched == targetLength:
                if (minright - minleft) > (right -left):
                    # print("in")
                    minright = right
                    minleft = left
                
                ans = s[minleft:minright+1]
                subArray[s[left]] -= 1
                if subArray[s[left]] < target[s[left]]:
                    matched -= 1
                left += 1
            
        return ans