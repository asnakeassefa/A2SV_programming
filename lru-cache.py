class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.store = OrderedDict()

    def get(self, key: int) -> int:  
        if key in self.store:
            val = self.store[key]
            del(self.store[key])
            self.store[key] = val
            return val
        else:
            return -1
    def put(self, key: int, value: int) -> None:
        if key in self.store:
            del(self.store[key])
            self.store[key] = value
        elif len(self.store) < self.capacity:
            self.store[key] = value
        else:
            self.store.popitem(last = False)
            self.store[key] = value

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)