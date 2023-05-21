class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        length = len(adjacentPairs) + 1
        indeg = defaultdict(int)
        graph = defaultdict(list)

        for adj in adjacentPairs:
            indeg[adj[0]] += 1
            indeg[adj[1]] += 1
            graph[adj[0]].append(adj[1])
            graph[adj[1]].append(adj[0])

        queue = deque()
    
        for key,val in indeg.items():
            if val == 1:
                queue.append(key)

        start = 0
        end = length-1
        ans = [0] * length
        print(graph)
        flag = True
        while queue:
            node = queue.popleft()
            if flag:
                ans[start] = node
                start += 1
                flag = False
            else:
                ans[end] = node
                end -= 1
                flag = True
            for value in graph[node]:
                indeg[value] -= 1
                if indeg[value] == 1:
                    queue.append(value)  
        return ans