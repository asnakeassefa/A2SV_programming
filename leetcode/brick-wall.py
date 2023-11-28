class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        count = defaultdict(int)
        for row in wall:
            val = list(accumulate(row))
            print(val)
            for num in val:
                count[num] += 1
        count[sum(wall[0])] = 0
        max_break = max(count.values())

        return len(wall) - max_break
