from typing import List
class Solution:
    def dfs(self,graph,color,curr, parent):
        if color[curr] == 2:
            return False
        if color[curr] == 1:
            return True
        
        color[curr] = 1
        for val in graph[curr]:
            if val != parent:
                cycle = self.dfs(graph,color,val, curr)
                if cycle:
                    return True
        color[curr] = 2
        return False
    #Function to detect cycle in an undirected graph.
    def isCycle(self, V: int, adj: List[List[int]]) -> bool:
        #Code here
        color = [0] * V
        for i in range(V):
            cycle = self.dfs(adj,color,i, -1)
            if cycle:
                return True
        
        return False