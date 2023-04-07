class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        store = Counter(deck)
        return reduce(math.gcd, store.values()) >= 2