class Website:
    def __init__(self, name , prev = None , next = None ):
        self.prev = prev
        self.next = next
        self.name = name

class BrowserHistory:
    def __init__(self, homepage: str):
        new_web = Website(homepage)
        self.current = new_web
        self.home = self.current

    def visit(self, url: str) -> None:
        new_web = Website(url , self.current , None)
        self.current.next = new_web
        self.current = new_web
        # print(self.current.prev.name , self.current.name)

    def back(self, steps: int) -> str:
        while steps > 0 and self.current.prev:
            self.current = self.current.prev
            steps -= 1
       
        # print(self.current.name)
        # print(" ")
        return self.current.name
        

    def forward(self, steps: int) -> str:
        # print(" ")
        # print("after forward" , steps ,"steps")
        while steps > 0 and self.current.next:
            self.current = self.current.next
            steps -= 1
        print(self.current.name)
        # print(" ")
        return self.current.name


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)