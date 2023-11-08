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

    def PrintFac(self, currenTab, inLine):
        self.op.PrintOp(currenTab, inLine)
        if self.fac is not None:
            print(" * ", end='' if inLine else '\n')
            self.fac.PrintFac(currenTab, inLine)

    def ExecFac(self, datapoints):
        opValue = self.op.EvalOp(datapoints)
        if self.fac is not None:
            facValue = self.fac.ExecFac(datapoints)
            return opValue * facValue
        else:
            return opValue