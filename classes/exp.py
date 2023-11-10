
class Exp:
    def __init__(self, tokenizer):
        self.tokenizer = tokenizer
        self.type = None
        self.fac = None
        self.exp = None

    def ParseExp(self):
        from classes.fac import Fac
        self.fac = Fac(self.tokenizer)
        self.fac.ParseFac()
        # Check if we are in the 1st, second, or third
        # <fac>|<fac>+<exp>|<fac>-<exp> 

        if self.tokenizer.getToken() in [22, 23]:
            # store the + or - and parse the exp
            self.exp = Exp(self.tokenizer)
            self.type = self.tokenizer.tokenName()
            self.tokenizer.skipToken()
            self.exp.ParseExp()

    def PrintExp(self, currentTab):
        # Print the expression in-line
        self.fac.PrintFac(currentTab, True)
        # If the type is not none then we know we're in the second branch
        if self.type is not None:
            print(str(self.type), end='')
            self.exp.PrintExp(0)

    def ExecExp(self, datapoints):
        # returns the value of the expression to the caller
        # Get the value of the factor
        facValue = self.fac.ExecFac(datapoints)
        if self.type is not None:
            # We are in the second branch, so we need to + or - that value with the expression
            expValue = self.exp.ExecExp(datapoints)
            if self.type == "+":
                return facValue + expValue
            elif self.type == "-":
                return facValue - expValue
            else:
                # We should never get this because Parsing should only allow + or -
                print("Execution Error: Exp type unsupported")
                exit()
        else:
            return facValue
