class MyStack:

    def __init__(self):
        self.stack = deque()
    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        temp = deque()
        while len(self.stack) > 1:
            temp.append(self.stack.popleft())
        ans = []
        if len(self.stack):
            ans = self.stack.popleft()
        self.stack = temp
        return ans
    def top(self) -> int:
        return self.stack[-1]

    def empty(self) -> bool:
        if not len(self.stack):
            return True
        return False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()