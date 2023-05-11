class Solution:
    def dfs(self,graph,colors,curr,topSort):
        if colors[curr] == 2:
            return False
        if colors[curr] == 1:
            return True

        colors[curr] = 1

        for node in graph[curr]:
            cycle = self.dfs(graph,colors,node,topSort)
            if cycle:
                return True

        colors[curr] = 2
        topSort.append(curr)
        return False

    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        length = len(graph)
        colors = [0] * length
        topSort = []

        for i in range(length):
            cycle = self.dfs(graph,colors,i,topSort)

        topSort.sort()
        return topSort