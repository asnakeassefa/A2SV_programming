class TrieNode:
    def __init__(self,val):
        self.val = val
        self.kids = defaultdict(None)
        self.count = 0
        self.isEOW = False

class Solution:
    def __init__(self):
        self.root = TrieNode('*')
    
    def insert(self,word):
        node = self.root
        for char in word:
            if char not in node.kids:
                node.kids[char] = TrieNode(char)
            node = node.kids[char]
            node.count += 1
    def pres(self, word):
        node = self.root
        ans = 0
        for char in word:
            node = node.kids[char]
            ans += node.count
        return ans
                
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        ans = []
        for word in words:
            self.insert(word)
        
        for word in words:
            ans.append(self.pres(word))

        return ans