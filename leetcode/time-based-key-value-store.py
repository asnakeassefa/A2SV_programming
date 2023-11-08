from sortedcontainers import SortedSet

class TimeMap:
    def __init__(self):
        self.store = defaultdict(SortedSet)
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].add((timestamp,value))
    def get(self, key: str, timestamp: int) -> str:
        if not self.store[key] or self.store[key][0][0] > timestamp:
            return ""
        times = self.store[key]
        right = bisect_right(times,(timestamp,'z'))
        right = min(right,len(times)-1)
        if times[right][0] > timestamp:
            right = right - 1
        return times[right][1]

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)