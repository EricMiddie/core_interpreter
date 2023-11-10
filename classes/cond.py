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
        # Can start with (, !, [
        # type will either be (, !, && or ||. We know && and || start with [
        if self.tokenizer.getToken() not in [20, 15, 16]:
            print("Parse Error: Expected condition starting with (, !, or [")
            exit()
        if self.tokenizer.getToken() == 20:
            # Store the type and parse the comp
            self.type = self.tokenizer.getToken()
            self.comp = Comp(self.tokenizer)
            self.comp.ParseComp()
        elif self.tokenizer.getToken() == 15:
            #store the type and parse the cond
            self.type = self.tokenizer.getToken()
            self.cond1 = Cond(self.tokenizer)
            # skip the !
            self.tokenizer.skipToken()
            self.cond1.ParseCond()
        elif self.tokenizer.getToken() == 16:
            # Store the type and parse two conds
            self.cond1 = Cond(self.tokenizer)
            self.cond2 = Cond(self.tokenizer)
            # skip the [
            self.tokenizer.skipToken()

            self.cond1.ParseCond()
            # Check that there is a && or ||
            if self.tokenizer.getToken() not in [18, 19]:
                print("Parse Error: Expected && or || inbetween conditions")
                exit()
            # Store the token name and parse the second condition
            self.type = self.tokenizer.tokenName()
            self.tokenizer.skipToken()
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

    def EvalCond(self, datapoints):
        # Check what branch we're in by seeing which is still "None"
        if self.comp is not None:
            return self.comp.EvalComp(datapoints)
        elif self.cond2 is not None:
            cond1Value = self.cond1.EvalCond(datapoints)
            if self.type == "&&":
                # We can short circuit the AND operation if the first condition is false
                if not cond1Value:
                    return False
                    
                cond2Value = self.cond2.EvalCond(datapoints)
                return (cond1Value and cond2Value)
            elif self.type == "||":
                # We can short circuit the OR operation if the first condition is true
                if cond1Value:
                    return True
                
                cond2Value = self.cond2.EvalCond(datapoints)
                return (cond1Value or cond2Value)
        else:
            return (not self.cond1.EvalCond(datapoints))