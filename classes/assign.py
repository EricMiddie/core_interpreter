from classes.exp import Exp
from classes.iden import Id

class Assign:
    def __init__(self, tokenizer):
        self.id = None
        self.exp = None
        self.tokenizer = tokenizer

    def ParseAssign(self):
        # Make sure we're on an ID
        if self.tokenizer.getToken() != 32:
            print("Parse Error: Expected id to start assignment")
            exit()

        # skip the name and check for =. Skip if it is there
        name = self.tokenizer.idName()
        if not Id.IdDeclared(name):
            print("Parse Error: Attempted assign to undeclared id ("+name+")")
            exit()
        self.id = name
        self.tokenizer.skipToken()
        if self.tokenizer.getToken() != 14:
            print("Parse Error: Expected '=' after ID  to be assigned to")
            exit()
        self.tokenizer.skipToken()

        self.exp = Exp(self.tokenizer)
        self.exp.ParseExp()
        
        # check and skip the ;
        if self.tokenizer.getToken() != 12:
            print("Parse Error: Assignment must terminate with a ;")
            exit()
        self.tokenizer.skipToken()

    def PrintAssign(self, currentTab):
        tabs = '\t' * currentTab
        print(f"{tabs}{self.id} = ", end='')
        self.exp.PrintExp(0)
        print(";")

    def ExecAssign(self, datapoints):
        Id.AssignIdValue(self.id, self.exp.ExecExp(datapoints))


        