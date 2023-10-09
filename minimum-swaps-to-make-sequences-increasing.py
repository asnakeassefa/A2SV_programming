class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        
        def dp(idx,swaped,memo):
            if idx >= len(nums1):
                return 0
            if (idx,swaped) in memo:
                return memo[idx,swaped]
            res1 = float('inf')
            res2 = float('inf')
            if idx == 0 or nums1[idx] > nums1[idx-1] and nums2[idx] > nums2[idx-1]:
                res1 = dp(idx + 1,False,memo)
            
            if idx == 0 or nums1[idx] > nums2[idx-1] and nums2[idx] > nums1[idx-1]:
                res2 = dp(idx+1,True,memo) + 1

            memo[(idx,swaped)] = min(res1,res2)
            return memo[(idx,swaped)]
        return dp(0,False,{})