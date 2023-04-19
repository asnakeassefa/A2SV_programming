class Solution:
    def DFS(self,graph,ans,path,idx):
        if path[-1] == len(graph)-1:
            ans.append(path[:])
            return
        for num in graph[idx]:
            path.append(num)
            self.DFS(graph,ans,path,num)
            path.pop()
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans = []
        path = [0]
        self.DFS(graph,ans,path,0)
        return ans