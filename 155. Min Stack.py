class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        if self.stack[-1] == self.min_stack[-1]:
            self.min_stack.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]

mystack = MinStack()
mystack.push(-2)
mystack.push(0)
mystack.push(-3)
print(mystack.getMin()) # return -3
mystack.pop()
print(mystack.top())   # return 0
print(mystack.getMin()) # return -2