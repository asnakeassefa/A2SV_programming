class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        ans = float('inf')
        person = [0 for i in range(k)]
        def travers(idx,maxVal):
            nonlocal ans
            if ans <= maxVal:
                return
            
            if idx == len(cookies):
                ans = min(ans,maxVal)
                return
            
            for i in range(k):
                person[i] += cookies[idx]
                maxVal1 = max(maxVal,person[i])
                travers(idx+1,maxVal1)
                person[i] -= cookies[idx]
        travers(0,0)
        return ans