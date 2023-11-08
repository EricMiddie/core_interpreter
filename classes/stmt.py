from classes.assign import Assign
from classes.If import If
from classes.loop import Loop
from classes.io import In, Out

class Stmt:
    def __init__(self, tokenizer):
        # <assign>|<if>|<loop>|<in>|<out> put tokens for these as type
        self.tokenizer = tokenizer
        self.type = None
        self.value = None

    def ParseStmt(self):
        if self.tokenizer.getToken() not in [32, 5, 8, 10, 11]:
            print("Parse Error: Expected start of statement")
            exit()
        curToken = self.tokenizer.getToken()
        self.type = curToken
        if curToken == 32:
            self.value = Assign(self.tokenizer)
            self.value.ParseAssign()
        elif curToken == 5:
            self.value = If(self.tokenizer)
            self.value.ParseIf()
        elif curToken == 8:
            self.value = Loop(self.tokenizer)
            self.value.ParseLoop()
        elif curToken == 10: 
            self.value = In(self.tokenizer)
            self.value.ParseIn()
        elif curToken == 11:
            self.value = Out(self.tokenizer)
            self.value.ParseOut()

    def PrintStmt(self, currentTab):
        if type(self.value) is Assign:
            self.value.PrintAssign(currentTab)
        elif type(self.value) is If:
            self.value.PrintIf(currentTab)
        elif type(self.value) is Loop:
            self.value.PrintLoop(currentTab)
        elif type(self.value) is In:
            self.value.PrintIn(currentTab)
        elif type(self.value) is Out:
            self.value.PrintOut(currentTab)

    def ExecStmt(self, datapoints):
        if type(self.value) is Assign:
            self.value.ExecAssign(datapoints)
        elif type(self.value) is If:
            self.value.ExecIf(datapoints)
        elif type(self.value) is Loop:
            self.value.ExecLoop(datapoints)
        elif type(self.value) is In:
            self.value.ExecIn(datapoints)
        elif type(self.value) is Out:
            self.value.ExecOut(datapoints)

        

class StmtSeq:
    def __init__(self, tokenizer):
        self.stmt = None
        self.stmt_seq = None
        self.tokenizer = tokenizer

    def ParseStmtSeq(self):
        self.stmt = Stmt(self.tokenizer)
        # Make sure that it starts with an "int" 
        # <assign>|<if>|<loop>|<in>|<out> can be any of these
        if self.tokenizer.getToken() not in [32, 5, 8, 10, 11]:
                print("Error: Expected start of statement sequence")
                exit()
        self.stmt.ParseStmt()
        if self.tokenizer.getToken() in [32, 5, 8, 10, 11]:
            self.stmt_seq = StmtSeq(self.tokenizer)
            self.stmt_seq.ParseStmtSeq()

    def PrintStmtSeq(self, currentTab):
        self.stmt.PrintStmt(currentTab)
        if self.stmt_seq is not None:
            self.stmt_seq.PrintStmtSeq(currentTab)

    def ExecStmtSeq(self, datapoints):
        self.stmt.ExecStmt(datapoints)
        if self.stmt_seq is not None:
            self.stmt_seq.ExecStmtSeq(datapoints)
