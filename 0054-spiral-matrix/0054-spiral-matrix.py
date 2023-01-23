class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        while len(matrix) > 0:
            #poping first matrix
            if len(matrix) > 0:
                ans.extend(matrix.pop(0))
            #poping last element of remaing matrix
            for i in range(len(matrix)):
                if len(matrix[i]) > 0:
                    ans.append(matrix[i].pop())
            #poping bottom list and reverse the list
            if len(matrix) > 0:
                temp = matrix.pop()
                ans.extend(temp[::-1])
            #poping bottom to top of first elemnts
            for i in range(len(matrix)-1,-1,-1):
                if len(matrix[i]) > 0:
                    ans.append(matrix[i].pop(0))
            
        return ans
    