class Solution:
    def bfs(self,i,visited,colors,adj):
        queue = deque([i])
        colors[i] = 1
        while queue:
            node = queue.popleft()
            for val in adj[node]:
                if val in visited:
                    if colors[val] == colors[node]:
                        return False
                if colors[node] == 1:
                    colors[val] = 2
                elif colors[node] == 2:
                    colors[val] = 1
                if val not in visited:
                    queue.append(val)
                    visited.add(val)
        return True
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for dislike in dislikes:
            adj[dislike[0]].append(dislike[1])
            adj[dislike[1]].append(dislike[0])

        queue = deque([1])
        colors = [0] * (n+1)
        visited = set([1])
        
        for i in range(1,n+1):
            if colors[i] == 0:
                if not self.bfs(i,visited,colors,adj):
                    return False

        return True