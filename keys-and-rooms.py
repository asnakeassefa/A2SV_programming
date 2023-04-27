class Solution:
    def bfs(self,rooms):
        queue = deque([0])
        visited = set()
        i = 0
        while queue:
            i += 1
            node = queue.popleft()
            if node not in visited:
                visited.add(node)
                queue.extend(rooms[node])
        return len(visited)
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        return len(rooms) == self.bfs(rooms)