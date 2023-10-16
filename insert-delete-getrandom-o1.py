class RandomizedSet:

    def __init__(self):
        self.randomset = []
        self.store = defaultdict(int)
    def insert(self, val: int) -> bool:
        if val in self.store:
            return False
        else:
            self.store[val] = len(self.randomset)
            self.randomset.append(val)
            return True
    def remove(self, val: int) -> bool:
        if val in self.store:
            index = self.store[val]
            new_index = self.randomset[-1]
            self.randomset[index],self.randomset[-1] = self.randomset[-1],self.randomset[index]
            self.randomset.pop()
            self.store[new_index] = self.store[val]
            del(self.store[val])
            return True
        else:
            return False
    def getRandom(self) -> int:
        return random.choice(self.randomset)



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()