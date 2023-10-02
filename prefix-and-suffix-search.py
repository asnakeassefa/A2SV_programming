class WordFilter:

    def __init__(self, words: List[str]):
        self.comb = defaultdict()
        for k,word in enumerate(words):
            for i in range(len(word)):
                for j in range(len(word)):
                    self.comb[(word[:i+1], word[j:])] = k

    # def search(self,pref,suff):
        
    def f(self, pref: str, suff: str) -> int:
        if (pref,suff) in self.comb:
            return self.comb[(pref,suff)]
        return -1

# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)