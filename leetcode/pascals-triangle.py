class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1]]
        def rec(ans,row):
            if row > numRows:
                return ans
            last = ans[-1]
            new = [0] * row
            for i in range(row):
                x = i - 1
                if i >= len(last) or x < 0:
                    new[i] = 1
                    continue
                new[i] += last[i] + last[x]
            ans.append(new)
            return rec(ans,row+1)
        return rec(ans,2)