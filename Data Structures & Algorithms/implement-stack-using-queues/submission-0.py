from collections import deque
class MyStack:
    
    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)

    def pop(self) -> int:
        return self.q.pop()
        
    def top(self) -> int:
        popped = self.q.pop()
        self.q.append(popped)
        return popped

    def empty(self) -> bool:
        if not self.q:
            return True
        else:
            return False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()