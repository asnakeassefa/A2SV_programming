class Solution:
    def bfs(self,deadends,target):
        visited = set(tuple(deadends))
        queue= deque([[0,0,0,0]])
        count = 0
        while queue:
            length = len(queue)
            for _ in range(length):
                key = queue.popleft()
                value = ""
                for val in key:
                    value += str(val)
                if value == target:
                    return count
                if  value not in visited:
                    visited.add(value)
                    queue.extend(self.possible(key))
            count += 1
        return -1
    def possible(self,lock):
        result = []
        for i in range(4):
            lock[i] += 1
            lock[i] %= 10
            result.append(lock[:])

            lock[i] -= 2
            lock[i] %= 10
            result.append(lock[:])

            lock[i] += 1
            lock[i] %= 10
        return result
    def openLock(self, deadends: List[str], target: str) -> int:
        return self.bfs(deadends,target)