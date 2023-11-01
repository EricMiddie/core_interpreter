from classes.fac import Fac

class Exp:
    def __init__(self, tokenizer):
        # types: none, add, sub
        self.tokenizer = tokenizer
        self.type = None
        self.fac = None
        self.exp = None

    def ParseExp(self):
        print("Parsing Exp")
        self.fac = Fac(self.tokenizer)
        self.fac.ParseFac()

