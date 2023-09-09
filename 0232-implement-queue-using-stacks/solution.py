class MyQueue:
    def __init__(self):
        self.queue = []

    def push(self, x: int) -> None:
        self.queue = [x] + self.queue

    def pop(self) -> int:
        return self.queue.pop(-1)
        
    def peek(self) -> int:
        return self.queue[-1]
        
    def empty(self) -> bool:
        return self.queue == []
