class PiPiChecker:
    wordDic=["pipi","皮皮","felix","plpl","shrimp","虾"]
    def __init__(self):
        pass

    def checkContent(self,s):
        for word in self.wordDic:
            if word in s.lower().replace(" ",""):
                return True
        return False
