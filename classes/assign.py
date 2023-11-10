from classes.exp import Exp
from classes.iden import Id

class Assign:
    def __init__(self, tokenizer):
        self.id = None
        self.exp = None
        self.tokenizer = tokenizer

    def ParseAssign(self):
        # Make sure we're on an ID, this is redundant as the method will only be called when it finds an id
        if self.tokenizer.getToken() != 32:
            print("Parse Error: Expected id to start assignment")
            exit()

        name = self.tokenizer.idName()
        # check to make sure that the id has been declared
        if not Id.IdDeclared(name):
            print("Parse Error: Attempted assign to undeclared id ("+name+")")
            exit()
        # assign the name of the id to the object
        self.id = name
        self.tokenizer.skipToken()
        # Check and skip the =
        if self.tokenizer.getToken() != 14:
            print("Parse Error: Expected '=' after ID  to be assigned to")
            exit()
        self.tokenizer.skipToken()

        # initialize the expression and parse it
        self.exp = Exp(self.tokenizer)
        self.exp.ParseExp()
        
        # check and skip the ;
        if self.tokenizer.getToken() != 12:
            print("Parse Error: Assignment must terminate with a ;")
            exit()
        self.tokenizer.skipToken()

    def PrintAssign(self, currentTab):
        # tab over the required amount
        tabs = '\t' * currentTab
        print(f"{tabs}{self.id} = ", end='')
        # print the expression inline with no extra tabs
        self.exp.PrintExp(0)
        print(";")

    def ExecAssign(self, datapoints):
        # Call the function to assign the value to the specified id
        Id.AssignIdValue(self.id, self.exp.ExecExp(datapoints))


        