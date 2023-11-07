from classes.comp import Comp

class Cond:
    def __init__(self, tokenizer):
        # Choices: None, !, AND, OR
        self.tokenizer = tokenizer
        self.type = None 
        self.comp = None
        self.cond1 = None
        self.cond2 = None

    def ParseCond(self):
        # print("Parsing Cond")
        # Can start with (, !, [
        # type will either be (, !, && or ||. We know && and || start with [
        if self.tokenizer.getToken() not in [20, 15, 16]:
            print("Parse Error: Expected condition starting with (, !, or [")
            exit()
        if self.tokenizer.getToken() == 20:
            self.type = self.tokenizer.getToken()
            self.comp = Comp(self.tokenizer)
            self.comp.ParseComp()
        elif self.tokenizer.getToken() == 15:
            self.type = self.tokenizer.getToken()
            self.cond1 = Cond(self.tokenizer)
            # skip the !
            self.tokenizer.skipToken()
            self.cond1.ParseCond()
        elif self.tokenizer.getToken() == 16:
            self.cond1 = Cond(self.tokenizer)
            self.cond2 = Cond(self.tokenizer)
            # skip the [
            self.tokenizer.skipToken()

            self.cond1.ParseCond()
            if self.tokenizer.getToken() not in [18, 19]:
                print("Parse Error: Expected && or || inbetween conditions")
                exit()
            self.type = self.tokenizer.tokenName()
            self.cond2.ParseCond()
            #check and skip the ]
            if self.tokenizer.getToken() != 17:
                print("Parse Error: Expected closing ]")
                exit()
            self.tokenizer.skipToken()

    def PrintCond(self, currentTab):
        tabs = '\t'*currentTab
        if self.comp is not None:
            # this is the (
            print(f"{tabs}", end='')
            self.comp.PrintComp()
        elif self.cond2 is not None:
            # this is the [ with && or ||
            print(f"{tabs}[", end='')
            self.cond1.PrintCond(0)
            print(f" {self.type} ", end='')
            self.cond2.PrintCond(0)
            print("]", end='')

        else:
            # this is the !
            print(f"{tabs}!", end='')
            self.cond1.PrintCond(0)
            print(")", end='')