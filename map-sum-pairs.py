class TrieNode:
    def __init__(self,val):
        self.val = val
        self.sum = 0
        self.kids = defaultdict(None)
        self.isEOW = False
class MapSum:

    def __init__(self):
        self.root = TrieNode("*")
        self.dict = defaultdict(int)

    def sub(self,word,val):
        node = self.root
        for char in word:
            node.kids[char].sum -= val
            node = node.kids[char]
    def insert(self, key: str, val: int) -> None:
        if key in self.dict:
            self.sub(key,self.dict[key])
        self.dict[key] = val
        node = self.root
        for char in key:
            if char not in node.kids:
                node.kids[char] = TrieNode(char)
                node.kids[char].sum = val
            elif char in node.kids:
                node.kids[char].sum += val
            node = node.kids[char]
        node.isEOW = True

    def sum(self, prefix: str) -> int:
        node = self.root
        last = 0
        for char in prefix:
            if char in node.kids:
                node = node.kids[char]
            else:
                return 0
        return node.sum


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)