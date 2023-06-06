class Solution:
    def dp(self,triangle,index,idx,memo):
        if len(triangle) == len(triangle[index]):
            return triangle[index][idx]
        
        if (index,idx) in memo:
            return memo[(index,idx)]

        memo[(index,idx)] = min(self.dp(triangle,index+1,idx,memo),self.dp(triangle,index+1,idx+1,memo)) + triangle[index][idx]

        return memo[(index,idx)]
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        return self.dp(triangle,0,0,{})