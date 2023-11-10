from classes.cond import Cond

class Loop:
    def __init__(self, tokenizer):
        self.tokenizer = tokenizer
        self.cond = None
        self.stmt_seq = None

    def ParseLoop(self):
        from classes.stmt import StmtSeq
        # Initialize the condition and the statement sequence
        self.cond = Cond(self.tokenizer)
        self.stmt_seq = StmtSeq(self.tokenizer)

        # check and skip the 'while'
        if(self.tokenizer.getToken() != 8):
            print("Parse Error: Expected 'while' to start LOOP statement.")
            exit()
        self.tokenizer.skipToken()

        # Parse the condition
        self.cond.ParseCond()

        # Check for and skip the 'loop'
        if(self.tokenizer.getToken() != 9):
            print("Parse Error: Expected loop after conditional.")
            exit()
        self.tokenizer.skipToken()

        # Parse the statement sequence
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

    def PrintLoop(self, currentTab):
        # Print the 'while' at the current Tab
        tabs = '\t' * currentTab
        print(f"{tabs}while ", end='')
        # Print the condition in line
        self.cond.PrintCond(0)
        # We want it to go to the next line here
        print(" loop") 
        # Print statement sequence at an additional indent
        self.stmt_seq.PrintStmtSeq(currentTab + 1)
        print(f"{tabs}end;")

    def ExecLoop(self, datapoints):
        # Execute the while loop based on evaluating the condition
        while self.cond.EvalCond(datapoints):
            self.stmt_seq.ExecStmtSeq(datapoints)

    