class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        dist = [[float('inf')] * numCourses for _ in range(numCourses)]
        
        for i,j in prerequisites:
            dist[i][j] = 1
        
        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    dist[i][j] = min(dist[i][j],dist[i][k] + dist[k][j])
        ans = []
        for i,j in queries:
            ans.append(dist[i][j] != float('inf'))

        return ans