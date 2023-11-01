from classes.exp import Exp

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
        self.tokenizer.skipToken()
        if self.tokenizer.getToken() != 14:
            print("Parse Error: Expected '=' after ID  to be assigned to")
            exit()
        self.tokenizer.skipToken()

        self.exp = Exp(self.tokenizer)


        