class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        years = [0] * 101

        for log in logs:
            years[log[0] - 1950] += 1
            years[log[1] - 1950] -= 1
        years = list(accumulate(years))
        ans = 0
        for i,year in enumerate(years):
            if year > years[ans]:
                ans = i
        return ans + 1950