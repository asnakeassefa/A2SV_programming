class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        store = [0] * numCourses
        graph = defaultdict(list)
        
        for course in prerequisites:
            graph[course[0]].append(course[1])
            store[course[1]] += 1
        
        queue = deque()

        for i,value in enumerate(store):
            if value == 0:
                queue.append(i)
        
        while queue:
            node = queue.popleft()
            for value in graph[node]:
                store[value] -= 1
                if store[value] == 0:
                    queue.append(value)
        
        if sum(store):
            return False
        return True