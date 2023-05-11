class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        dep = [0] * n
        ans = [set() for i in range(n)]
        queue = deque()
        for num in edges:
            graph[num[0]].append(num[1])
            dep[num[1]] += 1

        for i in range(n):
            if dep[i] == 0:
                queue.append(i)
        while queue:
            node = queue.popleft()
            for value in graph[node]:
                ans[value] |= ans[node] | {node}
                dep[value] -= 1
                if dep[value] == 0:
                    queue.append(value)
        
        res = []
        for val in ans:
            res.append(sorted(list(val)))
        return res