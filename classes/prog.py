from classes.decl import DeclSeq
from classes.stmt import StmtSeq

class Prog:
    def __init__(self, tokenizer):
        self.tokenizer = tokenizer
        self.decl_seq = None
        self.stmt_seq = None

    def ParseProg(self):
        print("Parsing Program")
        # init the child nodes
        self.decl_seq = DeclSeq(self.tokenizer)
        self.stmt_seq = StmtSeq(self.tokenizer)

        # check and skip the "program"
        if(self.tokenizer.getToken() != 1):
            print("Expected 'program' to start the file.")
            exit()
        self.tokenizer.skipToken()

        # parse the decalration sequence
        self.decl_seq.ParseDeclSeq()

        # check and skip the "begin"
        if self.tokenizer.getToken() != 2: 
            print("Error: expected begin (Check your variable declarations)")
            exit()
        self.tokenizer.skipToken()

        # parse the statement sequence
        self.stmt_seq.ParseStmtSeq()

        # check and skip the "end"
        if self.tokenizer.getToken() != 3: 
            print("Error: expected end")
            exit()
        self.tokenizer.skipToken()








