class Solution:
    def dfs(self,curr,graph,hasApple,visited):
        if not graph[curr] and hasApple[curr]:
            return 2
        if curr in visited or not graph[curr]:
            return 0
        
        value = 0
        visited.add(curr)
        for val in graph[curr]:
            if val not in visited:
                value += self.dfs(val,graph,hasApple,visited)
        if curr == 0:
            return value
        if value > 0:
            return value + 2
        elif hasApple[curr]:
            return value + 2
        return 0
            
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = defaultdict(list)
        visited = set()
        if not edges:
            return 0
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        
        return self.dfs(0,graph,hasApple,visited)