from classes.exp import Exp

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
            print("Parse Error: Expected start of operation not found")
            exit()
        
        if currToken == 31:
            # store and skip over the integer
            self.type = 31
            self.value = self.tokenizer.intVal()
            self.tokenizer.skipToken()
        elif currToken == 32:
            # store and skip over the identifier
            self.type = 32
            self.value = self.tokenizer.idName()
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
