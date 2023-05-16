from typing import List
from collections import defaultdict,deque

class Solution:
    def minimumTime(self, n : int,m : int, edges : List[List[int]]) -> int:
        # code here
        indeg = [0] * (n + 1)
        graph = defaultdict(list)
        ans = [0] * (n + 1)
        
        for val1,val2 in edges:
            graph[val1].append(val2)
            indeg[val2] += 1
            
        time = 1
        queue = deque()
        for i,val in enumerate(indeg):
            if val == 0 and i != 0:
                queue.append(i)
        
        while queue:
            length = len(queue)
            for _ in range(length):
                node = queue.popleft()
                ans[node] = str(time)
                for val in graph[node]:
                    indeg[val] -= 1
                    if indeg[val] == 0:
                        queue.append(val)

            time += 1
        return " ".join(ans[1:])