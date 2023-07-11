class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        indeg = [0] * n
        graph = defaultdict(list)
        if n == 1:
            return [0]
        for edge in edges:
            indeg[edge[0]] += 1
            indeg[edge[1]] += 1
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        
        queue = deque()
        visited = set()
        for i,val in enumerate(indeg):
            if val == 1:
                queue.append(i)
                visited.add(i)

        while queue:
            length = len(queue)
            ans = []
            for i in range(length):
                node = queue.popleft()
                ans.append(node)
                visited.add(node)
                for value in graph[node]:
                    indeg[value] -= 1
                    if indeg[value] == 1 and value not in visited:
                        queue.append(value)
        return ans