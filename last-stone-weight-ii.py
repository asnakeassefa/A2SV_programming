class Solution:
    def dp(self,curr,stones,target,total,memo):
        if curr >= len(stones):
            return total
        if (curr,total) in memo:
            return memo[(curr,total)]
        ans = 0
        if stones[curr] + total > target:
            ans = max(ans,self.dp(curr+1,stones,target,total,memo))
        else:
            ans = max(ans,max(self.dp(curr+1,stones,target,total+stones[curr],memo),self.dp(curr+1,stones,target,total,memo)))
        memo[(curr,total)] = ans
        return ans

    def lastStoneWeightII(self, stones: List[int]) -> int:
        target = ceil(sum(stones)/2)
        nextTarget = sum(stones)//2
        memo = defaultdict(int)
        temp = self.dp(0,stones,target,0,memo)
        print(target,nextTarget)
        print(temp)
        ans = abs(temp - target)
        ans += abs(temp - nextTarget) 
        return ans