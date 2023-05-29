class Solution:
    def solve(self,idx,memo,cost):
        if idx == len(cost)-1:
            return cost[idx]
        if idx == len(cost):
            return 0
        
        if memo.get(idx):
            return memo[idx]

        memo[idx] = min(self.solve(idx+1,memo,cost)+cost[idx],(self.solve(idx+2,memo,cost) + cost[idx]))
        return memo[idx]
        
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = defaultdict(int)
        return min(self.solve(0,memo,cost),self.solve(1,memo,cost))