class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.token = {}
        self.timeToLive  = timeToLive
        self.count = 0
        

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.token[tokenId] = currentTime
        self.count += 1
    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.token and currentTime < self.token[tokenId] + self.timeToLive:
            self.token[tokenId] = currentTime

    def countUnexpiredTokens(self, currentTime: int) -> int:
        count = 0
        toBeDeleted = []
        for token in self.token:
            if currentTime - self.token[token] >= self.timeToLive:
                self.count -= 1
                toBeDeleted.append(token)
        for t in toBeDeleted:
            self.token.pop(t)
        return self.count


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)