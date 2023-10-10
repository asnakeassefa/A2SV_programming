class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for from_, to, cost in flights:
            graph[from_].append((to,cost))
        
        def djkstra(start):
            costs = {i:float('inf') for i in range(n)}
            visited = set()
            costs[start] = 0

            queue = deque()
            queue.append((start,0,0))

            while queue:
                curr_node,curr_cost, curr_count = queue.popleft()
                if curr_count > k:
                    continue
                for node, cost in graph[curr_node]:
                    new_cost = curr_cost + cost
                    
                    if new_cost < costs[node]:
                        costs[node] = new_cost
                        queue.append((node,new_cost,curr_count+1))
            return costs

        val = djkstra(src)
        if val[dst] == inf:
            return -1
        return val[dst]