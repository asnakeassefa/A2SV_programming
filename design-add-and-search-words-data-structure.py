class TrieNode:
    def __init__(self,val):
        self.val = val
        self.kids = defaultdict(None)
        self.isEOW = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode("*")

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.kids:
                node.kids[char] = TrieNode(char)
            node = node.kids[char]
        node.isEOW = True
    def dfs(self,word,node):
        for i,char in enumerate(word):
            if char == ".":
                ans = False
                for val in node.kids.values():
                    ans = ans or self.dfs(word[i+1:],val)
                    if ans:
                        return True
                return ans
            elif char not in node.kids:
                return False
            else:
                node = node.kids[char]
        return node.isEOW
    def search(self, word: str) -> bool:
        node = self.root
        return self.dfs(word,node)
# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)