class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        length = len(quiet)
        ans = [0] * length
        MinValues = quiet.copy()
        # print(MinValues)
        indeg = [0] * length
        graph = defaultdict(list)
        quiets = defaultdict(int)

        for i,level in enumerate(quiet):
            quiets[level] = i
        
        for person1,person2 in richer:
            graph[person1].append(person2)
            indeg[person2] += 1

        queue = deque()

        for i,val in enumerate(indeg):
            if val == 0:
                queue.append(i)

        while queue:
            node = queue.popleft()
            # print(node)
            for value in graph[node]:
                # print(value)
                indeg[value] -= 1
                # print(node,value)
                if MinValues[node] < MinValues[value]:
                    MinValues[value] = MinValues[node]
                if indeg[value] == 0:
                    queue.append(value)
        for i,val in enumerate(MinValues):
            ans[i] = quiets[val]
        return ans