class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        diff = []
        ans = 0
        for i,cost in enumerate(costs):
            diff.append((cost[0]-cost[1],i))
        diff.sort()
        ans = 0
        count = 0
        for val,idx in diff:
            if count < len(diff)//2:
                ans += costs[idx][0]
                count += 1
            else:
                ans += costs[idx][1]

        return ans