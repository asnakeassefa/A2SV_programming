class Solution:
    def findwinner(self, arr,left,right,p1):
        if left == right:
            if p1:
                return [arr[left],0]
            else:
                return [0,arr[left]]

        if p1:
            r = self.findwinner(arr,left,right-1,not p1)
            r[0] += arr[right]
            l = self.findwinner(arr,left+1,right,not p1)
            l[0] += arr[left]
            
            if l[0] >= r[0]:
                return l
            else:
                return r
        else:
            r = self.findwinner(arr,left,right-1,not p1)
            r[1] += arr[right]
            l = self.findwinner(arr,left+1,right,not p1)
            l[1] += arr[left]
            
            if l[1] >= r[1]:
                return l
            else:
                return r

    def PredictTheWinner(self, nums: List[int]) -> bool:
        score = self.findwinner(nums,0,len(nums)-1,True)
        return score[0] >= score[1]