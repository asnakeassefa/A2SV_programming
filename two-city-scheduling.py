class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        diffs = []
        length = len(costs)
        for i in range(length):
            diffs.append(((costs[i][0]- costs[i][1]),i))
        ans = 0
        j = length - 1
        diffs.sort()
        for i in range(length//2):
            ans += costs[diffs[i][1]][0]
            ans += costs[diffs[j-i][1]][1]
        print(diffs)
        return ans