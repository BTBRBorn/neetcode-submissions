class MinStack:
    def __init__(self):
        self.stack = []
        self.min_inds = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.min_inds):
            min_ind = self.min_inds[-1]
        else:
            min_ind = 0
            self.min_inds.append(0)
        if val < self.stack[min_ind]:
            self.min_inds.append(len(self.stack) - 1)

    def pop(self) -> None:
        self.stack.pop()
        index = len(self.stack)
        if index == self.min_inds[-1]:
            self.min_inds.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        if len(self.stack):
            min_index = self.min_inds[-1]
            return self.stack[min_index]