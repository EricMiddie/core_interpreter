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
        if self.tokenizer.getToken() not in [20, 15, 16]:
            print("Parse Error: Expected condition starting with (, !, or [")
            exit()
        if self.tokenizer.getToken() == 20:
            self.comp = Comp(self.tokenizer)
        elif self.tokenizer.getToken() == 15:
            self.cond1 = Cond(self.tokenizer)
            # skip the !
            self.tokenizer.skipToken()
            self.cond1.ParseCond()
        elif self.tokenizer.getToken == 16:
            self.cond1 = Cond(self.tokenizer)
            self.cond2 = Cond(self.tokenizer)
            # skip the [
            self.tokenizer.skipToken()

            self.cond1.ParseCond()
            if self.tokenizer.getToken() not in [18, 19]:
                print("Parse Error: Expected && or || inbetween conditions")

            #check and skip the ]
            if self.tokenizer.getToken() != 17:
                print("Parse Error: Expected closing ]")
            self.tokenizer.skip