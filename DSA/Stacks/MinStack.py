class MinStack(object):

    def __init__(self):
        self.S = []
        self.M = []

    def push(self, val):
        self.S.append(val)
        val = min(val, self.M[-1] if self.M else val)
        self.M.append(val)

    def pop(self):
        self.S.pop()
        self.M.pop()

    def top(self):
        return self.S[-1]
        
    def getMin(self):
        return self.M[-1]
        

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

### 

# Beats 84.64% python submissions in runtime
# Beats 93.37% python submissions in memory usage 