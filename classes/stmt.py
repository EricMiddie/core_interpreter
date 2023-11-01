from classes.assign import Assign

class Stmt:
    def __init__(self, type, value):
        # <assign>|<if>|<loop>|<in>|<out> put tokens for these as type
        self.type = type
        self.value = value

    def ParseStmt(self):
        print("Parsing Statement")
        if self.tokenizer.getToken() not in [32, 5, 9, 10, 11]:
            print("Error: Expected start of statement")
            exit()

        curToken = self.tokenizer.getToken()
        if curToken == 32:
            print ("Parse Assign")
        elif curToken == 5:
            print("Parse If")
        elif curToken == 9:
            print("Parse Loop")
        elif curToken == 10: 
            print("Parse In")
        elif curToken == 11:
            print("Parse Out")

        

class StmtSeq:
    def __init__(self, tokenizer):
        self.stmts = []
        self.tokenizer = tokenizer

    def ParseStmtSeq(self):
        print("Parsing Declaration Sequence")
        initStmt = Stmt(self.tokenizer)
        # Make sure that it starts with an "int" 
        # <assign>|<if>|<loop>|<in>|<out> can be any of these
        if self.tokenizer.getToken() not in [32, 5, 9, 10, 11]:
                print("Error: Expected start of statement sequence")
                exit()
        self.stmts.append(initStmt)
        initStmt.ParseStmt()
        while self.tokenizer.getToken() in [32, 5, 9, 10, 11]:
            initStmt = Stmt(self.tokenizer)
            self.stmts.append(initStmt)
            initStmt.ParseStmt()