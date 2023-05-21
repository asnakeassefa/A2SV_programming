class Solution:
    def dfs(self,graph,color,curr,parent,length,ans):
        if color[curr] == 2:
            return
        if color[curr] == 1:
            maxLen = length - parent[curr]
            ans[0] = max(ans[0],maxLen)
            return

        color[curr] = 1
        if graph[curr] > -1:
            if color[graph[curr]] != 1:
                parent[graph[curr]] = length+1
            self.dfs(graph,color,graph[curr],parent,length+1,ans)
            # if cycle[0]:
            #     return
        color[curr] = 2
        return
    
    def longestCycle(self, edges: List[int]) -> int:
        length = len(edges)
        color = [0] * length
        ans = [-1]
        parent = defaultdict(int)
        for i in range(length):
            self.dfs(edges,color,i,parent,0,ans)
            parent = defaultdict(int)
            
        return ans[0]