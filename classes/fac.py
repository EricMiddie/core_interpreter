from classes.op import Op

class Fac:
    def __init__(self, tokenizer):
        # Choices: op, multiplication
        self.tokenizer = tokenizer
        self.op = None
        self.fac = None

    def ParseFac(self):
        self.op = Op(self.tokenizer)
        # <int> | <id> | (<exp>) are possibilities
        self.op.ParseOp()
        # check if we are in the second condition of a fac
        if self.tokenizer.getToken() == 24:
            # skip the *, then store and parse the factor
            self.tokenizer.skipToken()
            self.fac = Fac(self.tokenizer)
            self.fac.ParseFac()

class CompOp:
    def __init__(self, operator):
        # Choices: !=, ==, <, >, <=, >=
        self.operator = operator