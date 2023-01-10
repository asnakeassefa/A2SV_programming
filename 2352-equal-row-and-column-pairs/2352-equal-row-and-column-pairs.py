class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        colValues = defaultdict(list)
        count = defaultdict(int)
        ans = 0
        for row in grid:
            length = len(row)
            for col in range(length):
                colValues[col].append(row[col])
        
        for value in colValues.values():
            count[tuple(value)] += 1
        
        for row in grid:
            ans += count[tuple(row)]
        
        return ans