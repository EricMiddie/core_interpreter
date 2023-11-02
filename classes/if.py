from classes.cond import Cond    

class If:
    def __init__(self, tokenizer):
        self.tokenizer = tokenizer
        self.cond = None
        self.stmt_seq_then = None
        self.stmt_seq_else = None
    
    def ParseIf(self):
        # check and skip the if
        # this is probably redundent
        if self.tokenizer.getToken() != 5:
            print("Parse Error: Expected IF to start with if")
            exit()
        
        self.cond = Cond(self.tokenizer)