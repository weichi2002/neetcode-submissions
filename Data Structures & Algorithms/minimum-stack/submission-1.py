class MinStack:

    def __init__(self):
        self.minStack = []
        self.stack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        
        if len(self.minStack) == 0:
            self.minStack.append(val)
            return 

        if val < self.getMin():
            self.minStack.append(val)
        else:
            self.minStack.append(self.getMin())

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minStack[-1]
        
