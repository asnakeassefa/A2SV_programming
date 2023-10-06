class Solution:
    def djkstra(self,graph,start):
        distances = defaultdict(float)
        distances[start] = 1
        visited = set()
        p_queue = [(-1,start)]
        while p_queue:
            curr_dist, curr_node = heappop(p_queue)
            if curr_node in visited:
                continue
            visited.add(curr_node)

            for n,w in graph[curr_node]:
                dist = (-curr_dist) * w
                if dist > distances[n]:
                    distances[n] = dist
                    heappush(p_queue,((-dist),n))

        return distances
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = defaultdict(list)
        for i,edge in enumerate(edges):
            graph[edge[0]].append((edge[1],succProb[i]))
            graph[edge[1]].append((edge[0],succProb[i]))
        
        distances = self.djkstra(graph,start_node)
        return distances[end_node]