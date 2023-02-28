class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        length = len(arr)
        left1 = 0
        left2 = 0
        ans1 = 1
        ans2 = 1
        tempright = 0
        #odd loop
        for right in range(1,length):
            if arr[right-1] <= arr[right] and (right-1) % 2 != 0 or arr[right-1] >= arr[right] and (right-1) % 2 == 0:
                left1 = right
            ans1 = max(ans1,right-left1+1)
        #even loop
        for right in range(1,length):
            if arr[right-1] <= arr[right] and (right-1) % 2 == 0 or arr[right-1] >= arr[right] and (right-1) % 2 != 0:
                left2 = right
            ans2 = max(ans2,right-left2+1)
        # print(ans1,ans2)
        #final answer
        ans = max(ans1,ans2)
        return ans