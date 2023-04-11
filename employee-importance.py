"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def DFS(self,employees,id,ans):
        for sub in employees:
            if sub.id == id:
                ans[0] += sub.importance
                for emp in sub.subordinates:
                    self.DFS(employees,emp,ans)
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        ans = [0]
        self.DFS(employees,id,ans)
        return ans[0]