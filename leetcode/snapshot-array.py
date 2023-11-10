class SnapshotArray:

    def __init__(self, length: int):
        self.store = defaultdict(list)
        for i in range(length):
            self.store[i] = [(0,0)]
        self.count = 0
    
    def set(self, index: int, val: int) -> None:
        # if self.count == len(self.arr[index])-1:
        #     self.arr[index] = [val]
        # elif self.count >= len(self.arr[index]):
        #     self.arr[index].append(val)
        #     print(self.arr)
        self.store[index].append((self.count,val))
    def snap(self) -> int:
        self.count += 1
        return self.count - 1

    def get(self, index: int, snap_id: int) -> int:
        val = self.store[index]
        idx = bisect_right(val,(snap_id,float('inf')))
        if idx > len(val)-1 or val[idx][0] > snap_id:
            idx -= 1
        return val[idx][1]

# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)