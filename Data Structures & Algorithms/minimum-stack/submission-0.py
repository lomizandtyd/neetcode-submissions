class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minstack:
            val = min(val, self.minstack[-1])
        self.minstack.append(val)
        

    def pop(self) -> None:
        self.stack.pop(-1)
        self.minstack.pop(-1)
        

    def top(self) -> int:
        return self.stack[-1]        

    def getMin(self) -> int:
        return self.minstack[-1]
        
