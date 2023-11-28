class StockSpanner:

    def __init__(self):
        self.span = []

    def next(self, price: int) -> int:
        count = 1
        while self.span and self.span[-1][0] <= price:
            count += self.span.pop()[1]
        self.span.append((price,count))
        return count

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)