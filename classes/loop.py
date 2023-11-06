from classes.cond import Cond

class Loop:
    def __init__(self, tokenizer):
        self.tokenizer = tokenizer
        self.cond = None
        self.stmt_seq = None

    def ParseLoop(self):
        from classes.stmt import StmtSeq
        self.cond = Cond(self.tokenizer)
        self.stmt_seq = StmtSeq(self.tokenizer)

        if(self.tokenizer.getToken() != 8):
            print("Parse Error: Expected 'while' to start LOOP statement.")
            exit()
        self.tokenizer.skipToken()

        self.cond.ParseCond()

        if(self.tokenizer.getToken() != 9):
            print("Parse Error: Expected loop after conditional.")
            exit()
        self.tokenizer.skipToken()

        self.stmt_seq.ParseStmtSeq()

        # Check and skip 'end' and ';'
        if(self.tokenizer.getToken() != 3):
            print("Parse Error: Expected end after statement sequence for loop.")
            exit()
        self.tokenizer.skipToken()

        if(self.tokenizer.getToken() != 12):
            print("Parse Error: Expected ; after the 'end'")
            exit()
        self.tokenizer.skipToken()

    