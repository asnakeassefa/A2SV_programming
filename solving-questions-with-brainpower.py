class Solution:
    def dp(self,questions,index,memo):
        if index >= len(questions):
            return 0
        
        if index in memo:
            return memo[index]
        
        x = self.dp(questions,index+questions[index][1]+1,memo) + questions[index][0]
        y = self.dp(questions,index+1,memo)
        memo[index] = max(x,y)
        return memo[index]

    def mostPoints(self, questions: List[List[int]]) -> int:
        return self.dp(questions,0,{})