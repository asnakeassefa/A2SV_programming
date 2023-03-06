class StockSpanner:
    def __init__(self):
        self.stack = []
        self.counter = defaultdict(int)
        self.span = 0
        self.idx = 0
    def next(self, price: int) -> int:
        self.counter[price] += 1
        while self.stack and self.stack[-1] <= price:
            value = self.stack.pop()
            if price != value:
                self.counter[price] += self.counter[value]
                self.counter[value] = 0
        self.span = self.counter[price]
        self.stack.append(price)
        return self.span










# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)