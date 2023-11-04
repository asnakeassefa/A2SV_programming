class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        row = True
        while matrix:
            ans.extend(matrix.pop(0))
            temp = []
            for val in matrix:
                if val:
                    temp.append(val.pop())
            ans.extend(temp)
            if matrix:
                ans.extend(matrix.pop()[::-1])
            temp = []
            for val in matrix:
                if val:
                    temp.append(val.pop(0))
            ans.extend(temp[::-1])
        print(ans)
        return ans