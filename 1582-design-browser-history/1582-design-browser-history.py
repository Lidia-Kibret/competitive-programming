class Node:
    def __init__(self, val="", back=None, forward=None):
        self.val = val
        self.back = back
        self.forward = forward



class BrowserHistory:

    def __init__(self, homepage: str):
        self.current = Node(homepage)

        

    def visit(self, url: str) -> None:
         new_node = Node(url, self.current)
         self.current.forward = new_node
         self.current = new_node
        

    def back(self, steps: int) -> str:
        while steps > 0 and self.current.back != None:
            self.current = self.current.back
            steps -= 1

        return self.current.val
        

    def forward(self, steps: int) -> str:
        while steps > 0 and self.current.forward != None:
            self.current = self.current.forward
            steps -= 1
        return self.current.val
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)