from typing import List
from collections import deque
class Solution:
    
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		#Code here
		indeg = [0] * V
	    for i,nodes in enumerate(adj):
	        for node in nodes:
	            indeg[node] += 1
	      
        queue = deque()
        for i in range(V):
            if indeg[i] < 2:
                queue.append(i)
        
        counter = 0
        while queue:
            node = queue.popleft()
            
            counter += 1
            for val in adj[node]:
                # for val in values:
                    indeg[val] -= 1
                    if indeg[val] == 1:
                        queue.append(val)
                
        if counter != V:
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