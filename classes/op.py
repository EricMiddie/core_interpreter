from classes.exp import Exp
from classes.iden import Id

class Op:
    def __init__(self, tokenizer):
        # Choices: int, id, expression
        self.tokenizer = tokenizer
        self.type = None
        self.value = None
    def ParseOp(self):
        currToken = self.tokenizer.getToken()
        # <int> | <id> | (<exp>) are possible
        if currToken not in [31, 32, 20]:
            print("Parse Error: Expected int value, id, or expression")
            exit()
        
        if currToken == 31:
            # store and skip over the integer
            self.type = 31
            self.value = self.tokenizer.intVal()
            self.tokenizer.skipToken()
        elif currToken == 32:
            # store and skip over the identifier
            self.type = 32
            name = self.tokenizer.idName()
            self.value = name
            # check if Id has been delcared
            if not Id.IdDeclared(name):
                print("Parse Error: undeclared variable ("+name+")")
                exit()
            self.tokenizer.skipToken()
        elif currToken == 20:
            # store and parse the expression
            self.type = 20
            self.value = Exp(self.tokenizer)
            # skip the (
            self.tokenizer.skipToken()
            # Parse the expression
            self.value.ParseExp()

            # check for and skip the )
            if self.tokenizer.getToken() != 21:
                print("Parse Error: Expected closing )")
                exit()
            self.tokenizer.skipToken()


    def PrintOp(self, currentTab, inLine):
        tabs = '\t' * currentTab
        if self.type in [31, 32]:
            # We print the "int" or ID
            print(f"{tabs}{self.value}", end='' if inLine else '\n')
        elif self.type == 20:
            # We print the (exp)
            print(f"{tabs}(", end='' if inLine else '\n')
            # Exp are printed inline by default
            self.value.PrintExp(0)
            print(")", end='' if inLine else '\n')

    def EvalOp(self, datapoints):
        if self.type == 31:
            return int(self.value)
        elif self.type == 32:
            return int(Id.GetIdValue(self.value))
        elif self.type == 20:
            return self.value.ExecExp(datapoints)