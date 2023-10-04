class Solution:
    def dijkstra(self,graph,start,n):
        times = [float('inf') for i in range(n+1)]
        times[start] = 0
        visited = set()

        queue = [(0,start)]
        while queue:
            curr_distance, curr_node = heappop(queue)
            if curr_node in visited:
                continue
            visited.add(curr_node)

            for neighbor, weight in graph[curr_node]:
                time = curr_distance + weight
                if time < times[neighbor]:
                    times[neighbor] = time
                    heappush(queue,(time,neighbor))
        return times
    
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)

        for u,v,w in times:
            graph[u].append((v,w))

        ans = max(self.dijkstra(graph,k,n)[1:])
        if ans == float('inf'):
            return -1
        return ans