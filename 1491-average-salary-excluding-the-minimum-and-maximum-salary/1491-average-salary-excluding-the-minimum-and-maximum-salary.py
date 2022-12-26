class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        SUM = sum(salary[1:-1])
        
        return SUM/len(salary[1:-1])