class MinStack:

    def __init__(self):
        self.container = []
        self.mins = []

    def push(self, val: int) -> None:
        self.container.append(val)
        if self.mins:
            self.mins.append(min(val, self.mins[-1]))
        else:
            self.mins.append(val)

    def pop(self) -> None:
        to_pop = self.container.pop()
        self.mins.pop()
        return to_pop

    def top(self) -> int:
        return self.container[-1]

    def getMin(self) -> int:
        return self.mins[-1]
