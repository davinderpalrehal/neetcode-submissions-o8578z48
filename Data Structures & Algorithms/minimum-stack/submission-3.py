class MinStack:

    def __init__(self):
        self.stack = []
        self.curr_min = {}

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.curr_min[len(self.stack)] = min(
            self.curr_min.get(
                len(self.stack) - 1,
                float('inf')
            ),
            val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.curr_min[len(self.stack)]
