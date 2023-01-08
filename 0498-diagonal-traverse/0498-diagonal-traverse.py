class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        
        n = len(mat)
        m = len(mat[0])
        index = defaultdict(list)
        ans = []
        
        #copying value in diagonal
        for i in range(n):
            for j in range(m):
                index[i+j].append(mat[i][j])
                
        # building the last answer
        for key,val in index.items():
            if key % 2 == 0:
                length = len(val) - 1
                for i in range(length,-1,-1):
                    ans.append(val[i])
            else:
                for value in val:
                    ans.append(value)
                    
        return ans