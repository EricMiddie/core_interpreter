
class Exp:
    def __init__(self, tokenizer):
        # types: none, add, sub
        self.tokenizer = tokenizer
        self.type = None
        self.fac = None
        self.exp = None

    def ParseExp(self):
        print("Parsing Exp")
        from classes.fac import Fac
        self.fac = Fac(self.tokenizer)
        self.fac.ParseFac()
        # Check if we are in the 1st, second, or third
        # <fac>|<fac>+<exp>|<fac>-<exp> 

        if self.tokenizer.getToken() in [22, 23]:
            # store the + or - and parse the exp
            self.exp = Exp(self.tokenizer)
            self.type = self.tokenizer.getToken()
            self.tokenizer.skipToken()
            self.exp.ParseExp()

