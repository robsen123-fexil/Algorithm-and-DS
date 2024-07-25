class MinStack:

    def __init__(self):
        self.stack=[]
        self.minstack=[]
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minstack:
            x=self.minstack[-1]
            value=min(x , val)
            self.minstack.append(value)
        else:
            self.minstack.append(val)


        

        

    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()
        

    def top(self) -> int:

        return self.stack[-1]
        self.minstack[-1]
        

    def getMin(self) -> int:
        
        return self.minstack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()