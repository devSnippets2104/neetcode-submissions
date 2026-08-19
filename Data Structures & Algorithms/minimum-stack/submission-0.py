class MinStack:

    def __init__(self):
        self.stack=[]
        self.min_stack=[]
        

    def push(self, val: int) -> None:
        self.stack.append(val)

        min_val=val if not self.min_stack else min(val,self.min_stack[-1])
        self.min_stack.append(min_val)
        

    def pop(self) -> None:
        if not self.min_stack:
            return 
        else:
            self.min_stack.pop()
            self.stack.pop()
        

    def top(self) -> int:
        if not self.stack:
            return -1
        else:
            return self.stack[-1]
        

    def getMin(self) -> int:
        if not self.min_stack:
            return -1
        else:
            return self.min_stack[-1]
        
