class BrowserHistory:

    def __init__(self, homepage: str):
        self.pages = [homepage]
        self.index = 0

    def visit(self, url: str) -> None:
        if self.index == len(self.pages) - 1:
            self.pages.append(url)
            self.index += 1
        else:
            self.pages = self.pages[:self.index+1]
            self.pages.append(url)
            self.index += 1

    def back(self, steps: int) -> str:
        new_index = self.index - steps
        if new_index < 0:
            new_index = 0
        self.index = new_index
        return self.pages[self.index]

    def forward(self, steps: int) -> str:
        new_index = self.index + steps
        if new_index >= len(self.pages):
            new_index = len(self.pages) - 1
        self.index = new_index
        return self.pages[self.index]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)