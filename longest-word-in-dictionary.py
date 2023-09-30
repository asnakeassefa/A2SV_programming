class TrieNode:
    def __init__(self,val):
        self.val = val
        self.kids = defaultdict(None)
        self.isEOW = False
class Solution:
    def __init__(self):
        self.root = TrieNode('*')
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.kids:
                node.kids[char] = TrieNode(char)
            node = node.kids[char]
        node.isEOW = True
    def search(self,word):
        node = self.root
        for char in word:
            node = node.kids[char]
            if not node.isEOW:
                return False
        return True
    def longestWord(self, words: List[str]) -> str:
        words.sort()
        for word in words:
            self.insert(word)
        ans = ""
        for word in words:
            if self.search(word) and len(word) > len(ans):
                ans = word
        return ans