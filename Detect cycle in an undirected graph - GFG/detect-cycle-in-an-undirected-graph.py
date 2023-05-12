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
#{ 
 # Driver Code Starts
if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isCycle(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends