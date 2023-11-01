from classes.decl import DeclSeq
from classes.stmt import StmtSeq

class Prog:
    def __init__(self, tokenizer):
        self.tokenizer = tokenizer
        self.decl_seq = None
        self.stmt_seq = None

    def ParseProg(self):
        if(self.tokenizer.getToken() != 1):
            print("Expected 'program' to start the file.")
            exit()
        # skip the "program"
        self.tokenizer.skipToken()

        self.decl_seq = DeclSeq(self.tokenizer)
        self.stmt_seq = StmtSeq(self.tokenizer)

        print(self.tokenizer.getToken())
        # self.decl_seq.ParseDeclSeq()
        # self.stmt_seq.parseDeclSeq()








